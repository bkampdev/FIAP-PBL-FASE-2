from dataclasses import dataclass
from datetime import datetime


@dataclass
class Modulo:
    nome_modulo : str
    prioridade_pouso: str
    nivel_combustivel: int
    massa: int
    criticidade_carga: str
    integridade_sensores: str
    horario_estimado_chegada : datetime
    
@dataclass
class CondicoesAmbiente:
    condicoes_atmosfericas: str
    disponibilidade_area: str