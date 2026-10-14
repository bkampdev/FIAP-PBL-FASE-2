from collections import deque

##codigos de prioridade utilizados no match ("switch")

CRITERIO_PRIORIDADE = 1
CRITERIO_COMBUSTIVEL = 2
CRITERIO_MASSA = 3
CRITERIO_CHEGADA = 4

## Pesquisa Simples - Busca Linear

def modulo_menor_combustivel(lista_de_modulos):
    """Retorna o menor combustível, ou None quando não há módulos."""
    if not lista_de_modulos:
        return None
    menor = lista_de_modulos[0]

    for i in range(1, len(lista_de_modulos)):
        if lista_de_modulos[i].nivel_combustivel < menor.nivel_combustivel:
            menor = lista_de_modulos[i]

    return menor


def modulo_maior_prioridade(lista_de_modulos):
    """Retorna o modulo de maior prioridade (1 = mais urgente, ou seja, o menor numero)."""
    if not lista_de_modulos:
        return None
    maior = lista_de_modulos[0]

    for i in range(1, len(lista_de_modulos)):
        if lista_de_modulos[i].prioridade_pouso < maior.prioridade_pouso:
            maior = lista_de_modulos[i]

    return maior


def modulos_por_criticidade(lista_de_modulos, criticidade):
    """Retorna todos os modulos com a criticidade de carga informada."""
    encontrados = []

    for i in range(0, len(lista_de_modulos)):
        if lista_de_modulos[i].criticidade_carga == criticidade:
            encontrados.append(lista_de_modulos[i])

    return encontrados



def valor_do_criterio(modulo, criterio):
    """Retorna o valor do atributo correspondente ao codigo do criterio.
    (match/case e o equivalente ao switch-case em Python)"""
    match criterio:
        case 1:
            return modulo.prioridade_pouso
        case 2:
            return modulo.nivel_combustivel
        case 3:
            return modulo.massa
        case 4:
            return modulo.horario_estimado_chegada
        case _:
            raise ValueError(f"Critério inválido: {criterio}")


def ordena_fila(fila, criterio):
    """Reorganiza a fila de pouso pelo criterio escolhido usando Bubble Sort."""
    # Valida mesmo quando a fila não tem pares para comparar.
    if criterio not in (CRITERIO_PRIORIDADE, CRITERIO_COMBUSTIVEL,
                       CRITERIO_MASSA, CRITERIO_CHEGADA):
        raise ValueError(f"Critério inválido: {criterio}")
    lista = list(fila)

    for i in range(0, len(lista)):
        for j in range(0, len(lista) - 1):
            # se o atual for maior que o proximo, troca os dois de lugar
            if valor_do_criterio(lista[j], criterio) > valor_do_criterio(lista[j + 1], criterio):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return deque(lista)
