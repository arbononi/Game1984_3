import getpass
from layouts.layouts import tela_login
from utils.userfunctions import *
from configs.config import *

class LoginView:
    _cancelar = False
    campos_login = {
        "login" : { "lin" : 16, "col" : 55, "size" : 20 },
        "senha" : { "lin" : 18, "col" : 55, "size" : 20 }
    }

    def __init__(self):
        pass

    def iniciar(self):
        limpar_tela()
        desenhar_tela(tela_login)
    
    def get_login(self):
        info = self.campos_login["login"]
        while True:
            limpar_linha()
            exibir_conteudo("↓", info["lin"] - 1, info["col"])
            exibir_mensagem("Informe o login de acesso ou digite CANCELAR para sair")
            posicionar_cursor(info["lin"], info["col"])
            login = input()
            if login.upper() == "CANCELAR":
                self._cancelar = True
            break
        exibir_conteudo(" ", info["lin"] - 1, info["col"])
        return login
    
    def get_senha(self):
        info = self.campos_login["senha"]
        limpar_linha()
        exibir_conteudo("↓", info["lin"] - 1, info["col"])
        exibir_mensagem("Informe a senha de acesso ou digite CANCELAR para sair")
        posicionar_cursor(info["lin"], info["col"])
        senha = getpass.getpass(prompt='')
        if senha.upper() == "CANCELAR":
            self._cancelar = True
        return senha
