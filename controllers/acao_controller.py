from models.models import Acao
from services.banco_repository import BancoRepository
from views import acao_view

class AcaoController:
    def __init__(self, banco: BancoRepository):
        self.banco = banco

    def cadastrar_acao(self, idlinha, tipoacao, possuiacaoautomatica, proximopasso):
        acao = Acao(idlinha=idlinha, tipoacao=tipoacao, possuiacaoautomatica=possuiacaoautomatica, proximopasso=proximopasso)
        acao.id = self.banco.inserir_acao(acao)
        return acao

    def exibir_acao(self, id):
        dados = self.banco.buscar_acao(id)  # Esse método deve retornar um dict ou Livro
        acao_view.exibir(dados)
