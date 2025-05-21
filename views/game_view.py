from utils.userfunctions import *
from models.session import Session
from layouts.layouts import tela_capitulos, titulos_tela
from configs.config import *
from models.models import *
from models.models_dto import *
from time import sleep

class GameView:
    def __init__(self):
        self.session = Session()
        self.progresso_usuario = None
        self.livro = None
        pass

    def iniciar(self, livro: LivroDTO, progresso_usuario: ProgressoUsuario):
        self.livro = livro
        self.progresso_usuario = progresso_usuario
        limpar_tela()
        limpar_linha(lin=2, col=3,size=93)
        desenhar_tela(tela_capitulos, line_loop=4, stop_loop=32)
        exibir_conteudo(f"{titulos_tela["tela_game"]}{self.session.user.login}", lin=2, col=4)
        if not self.progresso_usuario:
            capitulo = self.livro.capitulos[0]
            pagina = capitulo.paginas[0]
        else:
            capitulo = self.livro.capitulos[self.progresso_usuario.idcapitulo]
            pagina = capitulo[self.progresso_usuario.idpagina]
        while True:
            self.exibir_dados(capitulo, pagina)
            if capitulo.id == self.livro.capitulos.count():
                break
            if capitulo.numero_paginas == pagina.id:
                capitulo = self.livro.capitulos[capitulo.id - 1]
                pagina = capitulo.paginas[0]

    def exibir_dados(self, capitulo: CapituloDTO, pagina: PaginaDTO):
        self.limpar_area_texto()
        exibir_conteudo(f"Capítulo {capitulo.id}".center(75, " "), lin=4, col=4)
        lin = 5
        col = 4
        for linha in pagina.linhas:
            for letra in linha.conteudo:
                exibir_conteudo(letra, lin, col)
                sleep(0.05)
                col +=1
                if col == 76:
                    lin += 1
                    col = 4
                if lin == 32:
                    exibir_mensagem("Pressione qualquer tecla para continuar...", wait_key=True)
                    self.limpar_area_texto()
        exibir_mensagem("Pressione qualquer tecla para ir pra próxima página...", wait_key=True)

    def limpar_area_texto(self):
        for lin in range(4, 33):
            exibir_conteudo(" " * 75, lin, 4)
