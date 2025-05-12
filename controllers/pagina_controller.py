from models.models import Pagina
from services.banco_repository import BancoRepository
from views import pagina_view

class PaginaController:
    def __init__(self, banco: BancoRepository):
        self.banco = banco

    def cadastrar_pagina(self, idcapitulo, nrlinhas):
        pagina = Pagina(idcapitulo=idcapitulo, nrlinhas=nrlinhas)
        pagina.id = self.banco.inserir_pagina(pagina)
        return pagina

    def exibir_pagina(self, id):
        dados = self.banco.buscar_pagina(id)  # Esse método deve retornar um dict ou Livro
        pagina_view.exibir(dados)
