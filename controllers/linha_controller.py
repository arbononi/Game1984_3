from models.models import Linha
from services.banco_repository import BancoRepository
from views import linha_view

class LinhaController:
    def __init__(self, banco: BancoRepository):
        self.banco = banco

    def cadastrar_linha(self, idpagina, conteudo, possuiacao):
        linha = Linha(idpagina=idpagina, conteudo=conteudo, possuiacao=possuiacao)
        linha.id = self.banco.inserir_linha(linha)
        return linha

    def exibir_linha(self, id):
        dados = self.banco.buscar_linha(id)  # Esse método deve retornar um dict ou Livro
        linha_view.exibir(dados)
