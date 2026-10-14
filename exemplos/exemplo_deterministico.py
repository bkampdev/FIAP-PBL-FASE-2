"""Executar na raiz: python3 -m exemplos.exemplo_deterministico."""
from datetime import datetime

import Consultas
import main
from Modulos import Modulo, CondicoesAmbiente


def criar_modulos():
    """Os seis tipos de Lorenzo, com atributos fixos e unidades do relatório."""
    return [
        Modulo("Transporte", 4, 50, 20, "Baixa", "Operacional", datetime(2026, 10, 12, 11)),
        Modulo("Comunicação", 3, 10, 12, "Média", "Falha parcial", datetime(2026, 10, 12, 8)),
        Modulo("Saúde", 1, 5, 10, "Alta", "Falha total", datetime(2026, 10, 12, 6)),
        Modulo("Energia", 2, 9, 15, "Alta", "Falha parcial", datetime(2026, 10, 12, 7)),
        Modulo("Segurança", 5, 90, 18, "Alta", "Operacional", datetime(2026, 10, 12, 12)),
        Modulo("Suprimentos", 3, 11, 14, "Média", "Operacional", datetime(2026, 10, 12, 9)),
    ]


def nomes(modulos):
    return [modulo.nome_modulo for modulo in modulos]


def executar():
    main.inicializar_simulacao(criar_modulos())
    print("Fila inicial:", nomes(main.modulos_fila_de_pouso))
    print("Menor combustível:", Consultas.modulo_menor_combustivel(main.modulos_definidos).nome_modulo)
    print("Maior prioridade:", Consultas.modulo_maior_prioridade(main.modulos_definidos).nome_modulo)
    print("Carga Alta:", nomes(Consultas.modulos_por_criticidade(main.modulos_definidos, "Alta")))

    for criterio, descricao in ((1, "prioridade"), (2, "combustível"),
                               (3, "massa"), (4, "chegada")):
        ordenada = Consultas.ordena_fila(main.modulos_fila_de_pouso, criterio)
        print(f"Ordenação por {descricao}:", nomes(ordenada))

    # Bubble Sort reorganiza; popleft atende a fila resultante em FIFO.
    ordenada = Consultas.ordena_fila(main.modulos_fila_de_pouso, Consultas.CRITERIO_PRIORIDADE)
    main.modulos_fila_de_pouso.clear()
    main.modulos_fila_de_pouso.extend(ordenada)
    ordem_processada = nomes(main.modulos_fila_de_pouso)
    ambientes_por_nome = {
        "Saúde": CondicoesAmbiente("Estável", "Livre"),
        "Energia": CondicoesAmbiente("Tempestade", "Ocupada"),
        "Comunicação": CondicoesAmbiente("Estável", "Livre"),
        "Suprimentos": CondicoesAmbiente("Estável", "Livre"),
        "Transporte": CondicoesAmbiente("Ventos fortes", "Livre"),
        "Segurança": CondicoesAmbiente("Estável", "Ocupada"),
    }
    main.decide_pouso([ambientes_por_nome[nome] for nome in ordem_processada])
    # Cópia antes do pop: evidência local do exemplo, sem persistência de auditoria.
    historico = main.historico_de_decisoes.copy()
    print("Fila após processamento:", nomes(main.modulos_fila_de_pouso))
    print("Pilha antes da exibição:", historico)
    main.exibe_resultado()
    print("Pilha após a exibição:", main.historico_de_decisoes)
    return {
        "ordem_processada": ordem_processada,
        "pousados": nomes(main.modulos_pousados),
        "espera": nomes(main.modulos_em_espera),
        "alerta": nomes(main.modulos_em_alerta),
        "historico": historico,
        "historico_apos_exibicao": main.historico_de_decisoes.copy(),
    }


if __name__ == "__main__":
    executar()
