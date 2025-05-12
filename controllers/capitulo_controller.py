from models.models import Capitulo
from services.banco_repository import BancoRepository
from views import capitulo_view

class CapituloController:
    def __init__(self, banco: BancoRepository):
        self.banco = banco

    def cadastrar_capitulo(self, idlivro, nrpaginas):
        capitulo = capitulo(idlivro=idlivro, nrpaginas=nrpaginas)
        capitulo.id = self.banco.inserir_capitulo(capitulo)
        return capitulo

    def exibir_capitulo(self, id_capitulo):
        dados = self.banco.buscar_capitulo(id_capitulo)  # Esse método deve retornar um dict ou Livro
        capitulo_view.exibir(dados)
