from models.models import AcaoAutomatica
from services.banco_repository import BancoRepository
from views import acao_automatica_view

class AcaoAutomaticaContoller:
    def __init__(self, banco: BancoRepository):
        self.banco = banco

    def cadastrar_acao_automatica(self, idacao, passosexecutar):
        acao_automatica = AcaoAutomatica(idacao=idacao, passosexecutar=passosexecutar)
        acao_automatica.id = self.banco.inserir_acao_automatica(acao_automatica)
        return acao_automatica

    def exibir_acao_automatica(self, id):
        dados = self.banco.buscar_acao_automatica(id)  # Esse método deve retornar um dict ou Livro
        acao_automatica_view.exibir(dados)
