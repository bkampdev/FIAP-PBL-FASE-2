
import unittest
from collections import deque
from datetime import datetime, timedelta

from Modulos import Modulo
import Consultas


class TestConsultas(unittest.TestCase):

    def setUp(self):
        chegada = datetime(2026, 10, 14, 10, 0)

        self.modulo_a = Modulo(
            "Modulo A", 3, 50, 1000,
            "Baixa", "Operacional", chegada
        )

        self.modulo_b = Modulo(
            "Modulo B", 1, 20, 2000,
            "Alta", "Operacional",
            chegada + timedelta(hours=2)
        )

        self.modulo_c = Modulo(
            "Modulo C", 2, 10, 1500,
            "Alta", "Operacional",
            chegada + timedelta(hours=1)
        )

        self.modulos = [
            self.modulo_a,
            self.modulo_b,
            self.modulo_c
        ]

    # TESTE 8 - Busca do menor combustivel
    def test_menor_combustivel(self):
        resultado = Consultas.modulo_menor_combustivel(
            self.modulos
        )
        self.assertEqual(resultado.nome_modulo, "Modulo C")

    # TESTE 9 - Busca da maior prioridade
    def test_maior_prioridade(self):
        resultado = Consultas.modulo_maior_prioridade(
            self.modulos
        )
        self.assertEqual(resultado.nome_modulo, "Modulo B")

    # TESTE 10 - Busca por criticidade
    def test_criticidade(self):
        resultado = Consultas.modulos_por_criticidade(
            self.modulos, "Alta"
        )

        nomes = [m.nome_modulo for m in resultado]

        self.assertEqual(nomes, ["Modulo B", "Modulo C"])

    # TESTE 11 - Ordenacao por prioridade
    def test_ordena_prioridade(self):
        fila = deque(self.modulos)

        resultado = Consultas.ordena_fila(
            fila, Consultas.CRITERIO_PRIORIDADE
        )

        nomes = [m.nome_modulo for m in resultado]

        self.assertEqual(
            nomes, ["Modulo B", "Modulo C", "Modulo A"]
        )

    # TESTE 12 - Ordenacao por combustivel
    def test_ordena_combustivel(self):
        fila = deque(self.modulos)

        resultado = Consultas.ordena_fila(
            fila, Consultas.CRITERIO_COMBUSTIVEL
        )

        nomes = [m.nome_modulo for m in resultado]

        self.assertEqual(
            nomes, ["Modulo C", "Modulo B", "Modulo A"]
        )

    # TESTE 13 - Ordenacao por massa
    def test_ordena_massa(self):
        fila = deque(self.modulos)

        resultado = Consultas.ordena_fila(
            fila, Consultas.CRITERIO_MASSA
        )

        nomes = [m.nome_modulo for m in resultado]

        self.assertEqual(
            nomes, ["Modulo A", "Modulo C", "Modulo B"]
        )

    # TESTE 14 - Ordenacao por chegada
    def test_ordena_chegada(self):
        fila = deque(self.modulos)

        resultado = Consultas.ordena_fila(
            fila, Consultas.CRITERIO_CHEGADA
        )

        nomes = [m.nome_modulo for m in resultado]

        self.assertEqual(
            nomes, ["Modulo A", "Modulo C", "Modulo B"]
        )

    # TESTE 15 - Criterio invalido
    def test_criterio_invalido(self):
        with self.assertRaises(ValueError):
            Consultas.ordena_fila(
                deque(self.modulos), 99
            )


if __name__ == "__main__":
    unittest.main()
