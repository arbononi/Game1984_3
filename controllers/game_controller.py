from services.banco_repository import BancoRepository
from views.game_view import GameView
from utils.userfunctions import *
from models.session import Session
from models.models import ProgressoUsuario

class GameController:
    def __init__(self, banco: BancoRepository):
        self.banco = banco
        self.session = Session()
        self.app = GameView()
        self.livro = None
        self.progresso_usuario = None

    def iniciar(self):
        self.livro = self.banco.carregar_livro_completo(1)
        self.progresso_usuario = self.banco.get_progresso_usuario(self.session.user.id)
        self.app.iniciar(livro=self.livro, progresso_usuario=self.progresso_usuario)
        exibir_conteudo("═", lin=3, col=80)
        exibir_conteudo("═", lin=33, col=80)
