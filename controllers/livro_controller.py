# controllers/livro_controller.py
from services.banco_repository import BancoRepository
from datetime import datetime
from models.models import Livro
from views.livro_view import *

class LivroController:
    def __init__(self, banco: BancoRepository):
        self.banco = banco

    def cadastrar_livro(self, titulo, autor):
        livro = Livro(titulo=titulo, autor=autor, data_cadastro=datetime.now())
        livro.id = self.banco.inserir_livro(livro)
        return livro

    def exibir_livro(self, id_livro):
        dados = self.banco.buscar_livro(id_livro)  # Esse método deve retornar um dict ou Livro
        exibir(dados)


    def mostrar_livro_completo(self, id_livro: int):
        livro = self.banco.carregar_livro_completo(id_livro)
        if livro:
            exibir_livro_completo(livro)
        else:
            print("Livro não encontrado.")
