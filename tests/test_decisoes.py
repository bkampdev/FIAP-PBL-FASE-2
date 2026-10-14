
import unittest
from unittest.mock import patch
from datetime import datetime
import runpy

from Modulos import Modulo, CondicoesAmbiente


class TestDecisoesPouso(unittest.TestCase):

    # TESTE 1 - Falha total dos sensores
    def test_falha_total_sensores(self):
        modulo = Modulo(
            nome_modulo="Modulo Teste",
            prioridade_pouso=1,
            nivel_combustivel=50,
            massa=1000,
            criticidade_carga="Baixa",
            integridade_sensores="Falha total",
            horario_estimado_chegada=datetime(2026, 10, 14, 10, 0)
        )

        ambiente = CondicoesAmbiente(
            condicoes_atmosfericas="Estável",
            disponibilidade_area="Livre"
        )

        with patch("Dados.gerar_modulo", return_value=modulo), \
             patch("Dados.gerar_condicoes_ambiente", return_value=ambiente), \
             patch("builtins.print"):

            resultado = runpy.run_module(
                "main", run_name="__main__"
            )

        self.assertEqual(len(resultado["modulos_em_alerta"]), 6)
        self.assertEqual(len(resultado["modulos_pousados"]), 0)
        self.assertEqual(len(resultado["modulos_em_espera"]), 0)

    # TESTE 2 - Combustivel em 9% (emergencia)
    def test_combustivel_9_emergencia(self):
        modulo = Modulo(
            nome_modulo="Modulo Emergencia",
            prioridade_pouso=1,
            nivel_combustivel=9,
            massa=1000,
            criticidade_carga="Alta",
            integridade_sensores="Operacional",
            horario_estimado_chegada=datetime(2026, 10, 14, 10, 0)
        )

        ambiente = CondicoesAmbiente(
            condicoes_atmosfericas="Estável",
            disponibilidade_area="Livre"
        )

        with patch("Dados.gerar_modulo", return_value=modulo), \
             patch("Dados.gerar_condicoes_ambiente", return_value=ambiente), \
             patch("builtins.print"):

            resultado = runpy.run_module(
                "main", run_name="__main__"
            )

        self.assertEqual(len(resultado["modulos_pousados"]), 6)
        self.assertEqual(len(resultado["modulos_em_alerta"]), 0)
        self.assertEqual(len(resultado["modulos_em_espera"]), 0)

    # TESTE 3 - Limites de combustivel (10% e 11%)
    def test_combustivel_10_e_11(self):
        for combustivel in [10, 11]:
            with self.subTest(combustivel=combustivel):
                modulo = Modulo(
                    nome_modulo="Modulo Limite",
                    prioridade_pouso=1,
                    nivel_combustivel=combustivel,
                    massa=1000,
                    criticidade_carga="Baixa",
                    integridade_sensores="Operacional",
                    horario_estimado_chegada=datetime(2026, 10, 14, 10, 0)
                )

                ambiente = CondicoesAmbiente(
                    condicoes_atmosfericas="Estável",
                    disponibilidade_area="Livre"
                )

                with patch("Dados.gerar_modulo", return_value=modulo), \
                     patch("Dados.gerar_condicoes_ambiente", return_value=ambiente), \
                     patch("builtins.print"):

                    resultado = runpy.run_module(
                        "main", run_name="__main__"
                    )

                self.assertEqual(
                    len(resultado["modulos_pousados"]), 6
                )
                self.assertEqual(
                    len(resultado["modulos_em_alerta"]), 0
                )
                self.assertEqual(
                    len(resultado["modulos_em_espera"]), 0
                )

    # TESTE 4 - Atmosfera instavel
    def test_atmosfera_instavel(self):
        modulo = Modulo(
            nome_modulo="Modulo Atmosfera",
            prioridade_pouso=1,
            nivel_combustivel=50,
            massa=1000,
            criticidade_carga="Baixa",
            integridade_sensores="Operacional",
            horario_estimado_chegada=datetime(2026, 10, 14, 10, 0)
        )

        ambiente = CondicoesAmbiente(
            condicoes_atmosfericas="Instável",
            disponibilidade_area="Livre"
        )

        with patch("Dados.gerar_modulo", return_value=modulo), \
             patch("Dados.gerar_condicoes_ambiente", return_value=ambiente), \
             patch("builtins.print"):

            resultado = runpy.run_module(
                "main", run_name="__main__"
            )

        self.assertEqual(len(resultado["modulos_em_espera"]), 6)
        self.assertEqual(len(resultado["modulos_pousados"]), 0)
        self.assertEqual(len(resultado["modulos_em_alerta"]), 0)

    # TESTE 5 - Area de pouso ocupada
    def test_area_ocupada(self):
        modulo = Modulo(
            nome_modulo="Modulo Area",
            prioridade_pouso=1,
            nivel_combustivel=50,
            massa=1000,
            criticidade_carga="Baixa",
            integridade_sensores="Operacional",
            horario_estimado_chegada=datetime(2026, 10, 14, 10, 0)
        )

        ambiente = CondicoesAmbiente(
            condicoes_atmosfericas="Estável",
            disponibilidade_area="Ocupada"
        )

        with patch("Dados.gerar_modulo", return_value=modulo), \
             patch("Dados.gerar_condicoes_ambiente", return_value=ambiente), \
             patch("builtins.print"):

            resultado = runpy.run_module(
                "main", run_name="__main__"
            )

        self.assertEqual(len(resultado["modulos_em_espera"]), 6)
        self.assertEqual(len(resultado["modulos_pousados"]), 0)
        self.assertEqual(len(resultado["modulos_em_alerta"]), 0)


if __name__ == "__main__":
    unittest.main()
