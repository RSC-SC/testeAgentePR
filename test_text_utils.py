"""Testes para o módulo text_utils."""

import unittest

from text_utils import (
    contar_palavras,
    normalizar_texto,
    palavras_mais_frequentes,
    remover_acentos,
)


class TestTextUtils(unittest.TestCase):

    def test_normalizar_texto_remove_espacos(self):
        self.assertEqual(normalizar_texto("  Olá   Mundo  "), "olá mundo")

    def test_normalizar_texto_vazio(self):
        self.assertEqual(normalizar_texto(""), "")

    def test_normalizar_texto_none(self):
        self.assertEqual(normalizar_texto(None), "")

    def test_contar_palavras(self):
        self.assertEqual(contar_palavras("um dois três"), 3)

    def test_palavras_mais_frequentes(self):
        texto = "gato cachorro gato peixe gato"
        self.assertEqual(
            palavras_mais_frequentes(texto, top_n=1),
            [("gato", 3)],
        )

    def test_remover_acentos(self):
        self.assertEqual(remover_acentos("coração"), "coracao")

    def test_remover_acentos_maiusculas(self):
        # Bug conhecido: acentos em maiúsculas não são removidos
        self.assertEqual(remover_acentos("OLÁ"), "OLA")


if __name__ == "__main__":
    unittest.main()
