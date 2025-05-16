import getpass
from datetime import datetime
from models.models import Usuario
from layouts.layouts import tela_usuarios, linha_opcoes, opcoes_disponiveis, titulos_tela
from utils.userfunctions import *
from configs.config import *

class Usuario_View:
    _usuario = None
    _cancelar = False
    campos_usuario = {
        "codigo" : { "lin" : 7, "col" : 20, "size" : 6 },
        "nome" : { "lin" : 7, "col" : 59, "size" : 20 },
        "login" : { "lin" : 7, "col" : 97, "size": 20 },
        "password" : { "lin" : 9, "col" : 20, "size" : 20 },
        "confirma" : { "lin" : 9, "col" : 59, "size" : 20 },
        "data_cadastro" : { "lin" : 9, "col" : 97, "size" : 10 }
    }

    def __init__(self):
        pass

    def iniciar(self):
        limpar_tela()
        desenhar_tela(tela_usuarios)
        exibir_conteudo(titulos_tela["cadastro_usuario"], lin=4, col=4)
        self.limpar_campos()

        while True:
            limpar_linha()
            posicionar_cursor(lin_message, col_message)
            opcao = exibir_mensagem(linha_opcoes["cadastro_usuarios"], wait_key=True)
            if opcao not in opcoes_disponiveis["cadastro_usuarios"]:
                limpar_linha
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                continue
            break
        if opcao == "R":
            exibir_conteudo("║", 5, 2)
            exibir_conteudo("║", 5, 119)
        return opcao
    
    def limpar_campos(self, desativar=True):
        for _, info in self.campos_usuario.items():
            exibir_conteudo("_" * info["size"], info["lin"], info["col"], desativar)

    def exibir_data_cadastro(self, data_cadastro: datetime):
        info = self.campos_usuario["data_cadastro"]
        str_data_cadastro = formatar_data(data_cadastro.date())
        exibir_conteudo(str_data_cadastro, info["lin"], info["col"])

    def get_codigo(self):
        info = self.campos_usuario["codigo"]
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        while True:
            try:
                limpar_linha()
                exibir_mensagem("Digite o código do usuário ou 0 para sair!")
                posicionar_cursor(info["lin"], info["col"])
                id_usuario = int(input())
                if id_usuario == 0:
                    self._cancelar = True
                break
            except ValueError as ex:
                exibir_mensagem("Código inválido!", wait_key=True)
                continue
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(str(id_usuario).rjust(6, " "), info["lin"], info["col"])
        return id_usuario
    
    def get_nome(self):
        info = self.campos_usuario["nome"]
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        while True:
            limpar_linha()
            exibir_mensagem("Informe o Nome do Usuário ou SAIR para encerrar!")
            posicionar_cursor(info["lin"], info["col"])
            nome = input()
            if nome.upper() == "SAIR":
                self._cancelar = True
                break
            if nome == "" and self._usuario is not None:
                nome = self._usuario.nome
            if nome == "":
                limpar_linha()
                exibir_mensagem("Nome do usuário não pode ficar em branco!", wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo(nome.title(), info["lin"], info["col"])
        return nome.title()

    def get_login(self):
        info = self.campos_usuario["login"]
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        while True:
            limpar_linha()
            exibir_mensagem("Informe o Login do usuário ou SAIR para encerrar!")
            posicionar_cursor(info["lin"], info["col"])
            login = input()
            if login.upper() == "SAIR":
                self._cancelar = True
                break
            if login == "" and self._usuario is not None:
                login = self._usuario.login
            if login == "":
                limpar_linha()
                exibir_mensagem("Login não pode ficar em branco!", wait_key=True)
                continue
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        return login
        
    def get_password(self):
        limpar_linha()
        info = self.campos_usuario["password"]
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        posicionar_cursor(info["lin"], info["col"])
        password = getpass.getpass(prompt='')
        if password.upper() == "SAIR":
            self._cancelar = True
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo("*" * len(password), info["lin"], info["col"])
        return password
    
    def get_confirmar_password(self):
        limpar_linha()
        info = self.campos_usuario["confirma"]
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        posicionar_cursor(info["lin"], info["col"])        
        confirmar_password = getpass.getpass(prompt='')
        if confirmar_password.upper() == "SAIR":
            self._cancelar = True
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        exibir_conteudo("*" * len(confirmar_password), info["lin"], info["col"])
        return confirmar_password
    
    def get_confirmar_dados(self):
        while True:
            limpar_linha()
            confirma = exibir_mensagem(linha_opcoes["confirmar_dados"], wait_key=True).upper()
            if confirma not in opcoes_disponiveis["confirmar_dados"]:
                limpar_linha()
                exibir_mensagem("Opção inválida! Tecle apenas S ou N!", wait_key=True)
                continue
            break
        return confirma

    def exibir_dados_usuario(self):
        for campo, info in self.campos_usuario.items():
            match campo:
                case "codigo":
                    exibir_conteudo(str(self._usuario.id).rjust(6, " "), info["lin"], info["col"])
                case "nome":
                    exibir_conteudo(self._usuario.nome.ljust(20, " "), info["lin"], info["col"])
                case "login":
                    exibir_conteudo(self._usuario.login.ljust(20, " "), info["lin"], info["col"])
                case "data_cadastro":
                    exibir_conteudo(formatar_data(self._usuario.data_cadastro.date()), info["lin"], info["col"])
                