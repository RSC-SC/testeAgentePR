"""Testes para o módulo number_utils."""

import unittest

from number_utils import (
    arredondar,
    eh_par,
    eh_primo,
    fatorial,
    formatar_moeda,
    media,
    porcentagem,
    raiz_quadrada,
    somar,
)


class TestNumberUtils(unittest.TestCase):

    def test_arredondar_padrao(self):
        self.assertEqual(arredondar(3.14159), 3.14)

    def test_arredondar_casas_customizadas(self):
        self.assertEqual(arredondar(3.14159, 3), 3.142)

    def test_arredondar_inteiro(self):
        self.assertEqual(arredondar(10, 0), 10.0)

    def test_arredondar_metade_para_cima(self):
        # Bug conhecido: round() usa arredondamento bancário
        self.assertEqual(arredondar(2.675, 2), 2.68)

    def test_formatar_moeda(self):
        self.assertEqual(formatar_moeda(1234.5), "R$ 1.234,50")

    def test_formatar_moeda_sem_centavos(self):
        self.assertEqual(formatar_moeda(10), "R$ 10,00")

    def test_porcentagem(self):
        self.assertEqual(porcentagem(25, 100), 25.0)

    def test_porcentagem_metade(self):
        self.assertEqual(porcentagem(1, 3), 33.33)

    def test_eh_par(self):
        self.assertTrue(eh_par(4))
        self.assertFalse(eh_par(7))

    def test_eh_primo(self):
        self.assertTrue(eh_primo(7))
        self.assertFalse(eh_primo(8))

    def test_fatorial_zero(self):
        self.assertEqual(fatorial(0), 1)

    def test_fatorial_cinco(self):
        self.assertEqual(fatorial(5), 120)

    def test_somar_lista(self):
        self.assertEqual(somar([1, 2, 3, 4]), 10)

    def test_somar_vazia(self):
        self.assertEqual(somar([]), 0)

    def test_raiz_quadrada(self):
        self.assertEqual(raiz_quadrada(16), 4.0)

    def test_media(self):
        self.assertEqual(media([2, 4, 6]), 4.0)


if __name__ == "__main__":
    unittest.main()