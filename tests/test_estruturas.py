
import unittest
from unittest.mock import patch
from datetime import datetime
import runpy

from Modulos import Modulo, CondicoesAmbiente


class TestEstruturas(unittest.TestCase):

    # TESTE 6 - Fila FIFO
    def test_fila_fifo(self):
        nomes = [
            "Modulo A",
            "Modulo B",
            "Modulo C",
            "Modulo D",
            "Modulo E",
            "Modulo F"
        ]

        modulos = [
            Modulo(
                nome_modulo=nome,
                prioridade_pouso=1,
                nivel_combustivel=50,
                massa=1000,
                criticidade_carga="Baixa",
                integridade_sensores="Operacional",
                horario_estimado_chegada=datetime(2026, 10, 14, 10, 0)
            )
            for nome in nomes
        ]

        ambiente = CondicoesAmbiente(
            condicoes_atmosfericas="Estável",
            disponibilidade_area="Livre"
        )

        with patch("Dados.gerar_modulo", side_effect=modulos), \
             patch("Dados.gerar_condicoes_ambiente", return_value=ambiente), \
             patch("builtins.print"):

            resultado = runpy.run_module(
                "main", run_name="__main__"
            )

        ordem_pouso = [
            modulo.nome_modulo
            for modulo in resultado["modulos_pousados"]
        ]

        self.assertEqual(ordem_pouso, nomes)
        self.assertEqual(len(resultado["modulos_fila_de_pouso"]), 0)

    # TESTE 7 - Pilha LIFO
    def test_pilha_lifo(self):
        nomes = [
            "Modulo A",
            "Modulo B",
            "Modulo C",
            "Modulo D",
            "Modulo E",
            "Modulo F"
        ]

        modulos = [
            Modulo(
                nome_modulo=nome,
                prioridade_pouso=1,
                nivel_combustivel=50,
                massa=1000,
                criticidade_carga="Baixa",
                integridade_sensores="Operacional",
                horario_estimado_chegada=datetime(2026, 10, 14, 10, 0)
            )
            for nome in nomes
        ]

        ambiente = CondicoesAmbiente(
            condicoes_atmosfericas="Estável",
            disponibilidade_area="Livre"
        )

        saidas = []

        with patch("Dados.gerar_modulo", side_effect=modulos), \
             patch("Dados.gerar_condicoes_ambiente", return_value=ambiente), \
             patch("builtins.print") as mock_print:

            runpy.run_module("main", run_name="__main__")

            for chamada in mock_print.call_args_list:
                argumentos = chamada.args

                if len(argumentos) == 2 and argumentos[0] == " -":
                    if ": Autorizado" in str(argumentos[1]):
                        saidas.append(argumentos[1])

        ordem_esperada = [
            f"{nome}: Autorizado"
            for nome in reversed(nomes)
        ]

        self.assertEqual(saidas, ordem_esperada)


if __name__ == "__main__":
    unittest.main()
