# models/models_dto.py
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class AcaoAutomaticaDTO:
    id: int
    passos_a_executar: str

@dataclass
class AcaoDTO:
    id: int
    tipo: str
    possui_acao_automatica: bool
    proximo_passo: Optional[int]
    acoes_automaticas: List[AcaoAutomaticaDTO] = field(default_factory=list)

@dataclass
class LinhaDTO:
    id: int
    conteudo: str
    possui_acao: bool
    acoes: List[AcaoDTO] = field(default_factory=list)

@dataclass
class PaginaDTO:
    id: int
    numero: int
    linhas: List[LinhaDTO] = field(default_factory=list)

@dataclass
class CapituloDTO:
    id: int
    numero_paginas: int
    paginas: List[PaginaDTO] = field(default_factory=list)

@dataclass
class LivroDTO:
    id: int
    titulo: str
    autor: str
    data_cadastro: datetime
    capitulos: List[CapituloDTO] = field(default_factory=list)
