from services.banco_repository import BancoRepository
from views.usuario_view import Usuario_View
from utils.userfunctions import exibir_mensagem, exibir_conteudo, limpar_linha, criar_hash_senha, verificar_senha
from models.models import Usuario
from datetime import datetime
from typing import Optional

class UsuarioController:
    def __init__(self, banco: BancoRepository):
        self.banco = banco
        self.app = Usuario_View()

    def iniciar(self):
        while True:
            opcao = self.app.iniciar()
            if opcao == "R":
                break
            match opcao:
                case "I":
                    self.incluir()
                case "A":
                    self.alterar()
                case "E":
                    limpar_linha()
                    exibir_mensagem("Opção em desenvolvimento!", wait_key=True)
                case "V":
                    limpar_linha()
                    exibir_mensagem("Opção em desenvolvimento!", wait_key=True)
                case "C":
                    limpar_linha()
                    exibir_mensagem("Opção em desenvolvimento!", wait_key=True)

    def incluir(self):
        self.app._usuario = None
        self.app._cancelar = False
        self.app.limpar_campos(False)
        info = self.app.campos_usuario["codigo"]
        exibir_conteudo("_" * info["size"], info["lin"] ,info["col"], True)
        data_cadastro = datetime.now()
        self.app.exibir_data_cadastro(data_cadastro)
        usuario, password, _ = self.get_dados_tela()
        confirmar_dados = self.app.get_confirmar_dados()
        if confirmar_dados != "S":
            return
        usuario.password = criar_hash_senha(password)
        usuario.data_cadastro = data_cadastro
        try:
            id_usuario = self.banco.inserir_usuario(usuario=usuario)
            exibir_mensagem(f"Usuário cadastrado com sucesso: Código: {id_usuario}", wait_key=True)
        except Exception as ex:
            limpar_linha()
            exibir_mensagem(ex, wait_key=True)

    def alterar(self):
        self.app._cancelar = False
        while True:
            id_usuario = self.app.get_codigo()
            if self.app._cancelar:
                return
            self.app._usuario = self.banco.buscar_usuario_por_id(id_usuario)
            if not self.app._usuario:
                limpar_linha()
                exibir_mensagem("Usuario não cadastrado!", wait_key=True)
                continue
            break
        self.app.exibir_dados_usuario()
        usuario, password, senha_alterada = self.get_dados_tela(True)
        confirmar_dados = self.app.get_confirmar_dados()
        if confirmar_dados != "S":
            return
        usuario.id = id_usuario
        if senha_alterada:
            usuario.password = criar_hash_senha(password)
        try:
            self.banco.atualizar_usuario(usuario=usuario, atualizar_senha=senha_alterada)
            exibir_mensagem(f"Usuário cadastrado com sucesso!", wait_key=True)
        except Exception as ex:
            limpar_linha()
            exibir_mensagem(f'Erro ao atualizar usuário: {ex}', wait_key=True)

    def get_dados_tela(self, alteracao=False):
        nome = self.app.get_nome()
        if self.app._cancelar:
            return
        while True:
            login = self.app.get_login()
            if self.app._cancelar:
                return None, None
            if self.app._usuario is not None:
                id_usuario = self.app._usuario.id
            else:
                id_usuario = 0
            login_free = self.banco.checar_login_disponivel(login, id_usuario)
            if not login_free:
                limpar_linha()
                exibir_mensagem("Login já cadastrado! Tente outro!", wait_key=True)
                continue
            break
        if alteracao:
            limpar_linha()
            alterar_senha = exibir_mensagem("Deseja alterar a senha (S/N)", wait_key=True)
        else:
            alterar_senha = "S"
        if alterar_senha == "S":
            password = self.app.get_password()
            if self.app._cancelar:
                return None, None
            senha_alterada = True
            while True:
                confirmar = self.app.get_confirmar_password()
                if self.app._cancelar:
                    return None, None
                if confirmar != password:
                    limpar_linha()
                    exibir_mensagem("Login não confere.!", wait_key=True)
                    continue
                break
        else:
            password = ''
            senha_alterada = False
        return Usuario(nome=nome, login=login), password, senha_alterada


        

