"""Complementa os testes de Davi com lacunas observadas na integração."""
import contextlib
import importlib
import io
import itertools
import unittest
from collections import deque
from datetime import datetime
from unittest.mock import patch

import Consultas
from Modulos import Modulo, CondicoesAmbiente


class TestIntegracao(unittest.TestCase):
    def test_buscas_vazias(self):
        self.assertIsNone(Consultas.modulo_menor_combustivel([]))
        self.assertIsNone(Consultas.modulo_maior_prioridade([]))
        self.assertEqual(Consultas.modulos_por_criticidade([], "Alta"), [])

    def test_criterio_invalido_em_fila_curta(self):
        for fila in (deque(), deque([None])):
            with self.subTest(tamanho=len(fila)):
                with self.assertRaises(ValueError):
                    Consultas.ordena_fila(fila, 99)

    def test_importar_main_nao_executa_simulacao(self):
        with patch("Dados.gerar_modulo") as gerar, patch("builtins.print") as imprimir:
            import main
            importlib.reload(main)
        gerar.assert_not_called()
        imprimir.assert_not_called()

    def test_portas_equivalem_a_decisao(self):
        import main
        # Cobre 3 estados de sensores x 5 combustíveis x 3 atmosferas x 3 áreas.
        for sensores, combustivel, atmosfera, area in itertools.product(
            ["Operacional", "Falha parcial", "Falha total"],
            [0, 9, 10, 11, 100],
            ["Estável", "Tempestade", "Ventos fortes"],
            ["Livre", "Ocupada", "Obstruída"],
        ):
            with self.subTest(sensores=sensores, combustivel=combustivel,
                              atmosfera=atmosfera, area=area):
                modulo = Modulo("Teste", 1, combustivel, 12, "Alta", sensores,
                                datetime(2026, 10, 12, 10))
                main.inicializar_simulacao([modulo])
                main.decide_pouso([CondicoesAmbiente(atmosfera, area)])
                f = sensores == "Falha total"
                e = combustivel < 10
                a = atmosfera == "Estável"
                p = area == "Livre"
                bloqueado = f
                emergencia = not f and e
                normal = not f and not e and a and p
                adiado = not f and not e and (not a or not p)
                self.assertEqual(sum([bloqueado, emergencia, normal, adiado]), 1)
                self.assertEqual(bool(main.modulos_em_alerta), bloqueado)
                self.assertEqual(bool(main.modulos_em_espera), adiado)
                self.assertEqual(bool(main.modulos_pousados), emergencia or normal)
                self.assertEqual("emergência" in main.historico_de_decisoes[-1], emergencia)

    def test_exemplo_fixo_com_consultas_e_estados(self):
        from exemplos.exemplo_deterministico import executar
        with contextlib.redirect_stdout(io.StringIO()) as saida:
            evidencia = executar()
        self.assertEqual(evidencia["ordem_processada"],
                         ["Saúde", "Energia", "Comunicação", "Suprimentos", "Transporte", "Segurança"])
        self.assertEqual(evidencia["pousados"], ["Energia", "Comunicação", "Suprimentos"])
        self.assertEqual(evidencia["espera"], ["Transporte", "Segurança"])
        self.assertEqual(evidencia["alerta"], ["Saúde"])
        self.assertEqual(evidencia["historico_apos_exibicao"], [])
        self.assertIn("Menor combustível: Saúde", saida.getvalue())
        self.assertIn("Energia: Autorizado (emergência)", saida.getvalue())

    def test_empates_preservam_ordem_e_fila_original(self):
        chegada = datetime(2026, 10, 12, 10)
        modulos = [Modulo(nome, 2, 50, 12, "Alta", "Operacional", chegada)
                   for nome in ("A", "B", "C")]
        fila = deque(modulos)
        for criterio in (1, 2, 3, 4):
            self.assertEqual(list(Consultas.ordena_fila(fila, criterio)), modulos)
        self.assertEqual(list(fila), modulos)
        self.assertEqual(Consultas.ordena_fila(deque(), 1), deque())


if __name__ == "__main__":
    unittest.main()
