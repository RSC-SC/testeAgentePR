"""Testes para o módulo email_utils."""

import unittest

from email_utils import (
    eh_email_institucional,
    extrair_dominio,
    extrair_usuario,
    mascarar_email,
    normalizar_email,
    validar_email,
)


class TestEmailUtils(unittest.TestCase):

    def test_validar_email_valido(self):
        self.assertTrue(validar_email("joao.silva@gmail.com"))

    def test_validar_email_sem_arroba(self):
        self.assertFalse(validar_email("joao.silva.gmail.com"))

    def test_validar_email_vazio(self):
        self.assertFalse(validar_email(""))

    def test_validar_email_none(self):
        self.assertFalse(validar_email(None))

    def test_extrair_usuario(self):
        self.assertEqual(extrair_usuario("joao.silva@gmail.com"), "joao.silva")

    def test_extrair_dominio(self):
        self.assertEqual(extrair_dominio("joao.silva@gmail.com"), "gmail.com")

    def test_extrair_dominio_minusculas(self):
        # Bug conhecido: domínio não é convertido para minúsculas
        self.assertEqual(extrair_dominio("joao@GMAIL.COM"), "gmail.com")

    def test_mascarar_email(self):
        self.assertEqual(mascarar_email("joao.silva@gmail.com"), "j********a@gmail.com")

    def test_mascarar_email_curto(self):
        self.assertEqual(mascarar_email("ab@empresa.com.br"), "a**@empresa.com.br")

    def test_normalizar_email(self):
        self.assertEqual(
            normalizar_email("  Joao.Silva@Gmail.COM  "),
            "joao.silva@gmail.com",
        )

    def test_normalizar_email_vazio(self):
        self.assertEqual(normalizar_email(""), "")

    def test_eh_email_institucional(self):
        self.assertTrue(eh_email_institucional("jose@empresa.com", ["empresa.com"]))

    def test_eh_email_institucional_dominio_diferente(self):
        self.assertFalse(eh_email_institucional("jose@gmail.com", ["empresa.com"]))


if __name__ == "__main__":
    unittest.main()