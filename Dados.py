import random
import Modulos 
import datetime   

NOMES_MODULOS = [
    "Saúde",
    "Segurança",
    "Energia",
    "Comunicação",
    "Suprimentos",
    "Transporte",
    ]
PRIORIDADE_MIN, PRIORIDADE_MAX = 1, 5
COMBUSTIVEL_MIN, COMBUSTIVEL_MAX = 0, 100 ## em porcentagem    
MASSA_MIN, MASSA_MAX = 10, 20  ##toneladas             
HORA_MIN, HORA_MAX = 6, 18                    
CRITICIDADE = ["Baixa", "Média", "Alta"]
SENSORES = ["Operacional", "Falha parcial", "Falha total"]
DATA_MISSAO = datetime.datetime(2026, 10, 12)  # data fixa da simulação

ATMOSFERA = ["Estável", "Tempestade", "Ventos fortes"]
AREA_POUSO = ["Livre", "Ocupada", "Obstruída"]

def gerar_horario_chegada():
    """Sorteia um horário entre HORA_MIN e HORA_MAX na data da missão."""
    hora = random.randint(HORA_MIN, HORA_MAX - 1)
    minuto = random.randint(0, 59)
    return DATA_MISSAO.replace(hour=hora, minute=minuto)


def gerar_modulo():
    return Modulos.Modulo(
        nome_modulo = random.choice(NOMES_MODULOS),
        prioridade_pouso=random.randint(PRIORIDADE_MIN, PRIORIDADE_MAX),
        nivel_combustivel=random.randint(COMBUSTIVEL_MIN, COMBUSTIVEL_MAX),
        massa=random.randint(MASSA_MIN, MASSA_MAX),
        criticidade_carga=random.choice(CRITICIDADE),
        horario_estimado_chegada=gerar_horario_chegada(),
        integridade_sensores=random.choice(SENSORES),
    )

def gerar_condicoes_ambiente():
    """Sorteia as condições externas no momento da tentativa de pouso."""
    return Modulos.CondicoesAmbiente(
        condicoes_atmosfericas=random.choice(ATMOSFERA),
        disponibilidade_area=random.choice(AREA_POUSO),
    )
