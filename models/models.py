from dataclasses import dataclass
from datetime import datetime

@dataclass
class Usuario:
    id: int = None
    nome: str = ""
    login: str = ""
    password: bytes = b""
    data_cadastro: datetime = datetime.now()
    
@dataclass
class Livro:
    id: int = None
    titulo: str = ""
    autor: str = ""
    data_cadastro: datetime = None


@dataclass
class Capitulo:
    idcapitulo: int = None
    idlivro: int = None
    nrpaginas: int = None

@dataclass
class Pagina:
    idpagina: int = None
    idcapitulo: int = None
    nrlinhas: int = None

@dataclass
class Linha:
    idlinha: int = None
    idpagina: int = None
    conteudo: str = ""
    possuiacao: int = None

@dataclass
class Acao:
    idacao: int = None
    idlinha: int = None
    tipoacao: str = ""
    possuiacaoautomatica: int = None
    proximopasso: str = ""

@dataclass
class AcaoAutomatica:
    idacaoautomatica: int = None
    idacao: int = None
    passosexecutar: str = ""
        