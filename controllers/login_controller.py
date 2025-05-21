from services.banco_repository import BancoRepository
from views.login_view import LoginView
from utils.userfunctions import *

class LoginController:
    def __init__(self, banco: BancoRepository):
        self.banco = banco
        self.app = LoginView()
        self.usuario = None

    def iniciar(self):
        self.app.iniciar()
        # Obtendo login do Usuário
        while True:
            self.app._cancelar = False
            login = self.app.get_login()
            if self.app._cancelar:
                break
            try:
                self.usuario = self.banco.buscar_usuario_por_login(login)
                if not self.usuario:
                    exibir_mensagem("Usuário não cadastrado!", wait_key=True)
                    continue
                break
            except Exception as ex:
                exibir_mensagem(f"Erro ao obter usuário: {ex}", wait_key=True)
                continue

        # Obtendo senha do usuário
        while True:
            senha = self.app.get_senha()
            if self.app._cancelar:
                break
            if not bcrypt.checkpw(senha.encode(), self.usuario.password):
                exibir_mensagem("Senha inválida!", wait_key=True)
                continue
            break
        limpar_linha()
        if self.app._cancelar:
            return None
        return self.usuario
        
            
