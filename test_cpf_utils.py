"""Testes para o módulo cpf_utils."""

import unittest

from cpf_utils import (
    extrair_digitos,
    formatar_cpf,
    gerar_cpf,
    mascarar_cpf,
    validar_cpf,
)


class TestCpfUtils(unittest.TestCase):

    def test_validar_cpf_valido(self):
        self.assertTrue(validar_cpf("529.982.247-25"))

    def test_validar_cpf_sem_mascara(self):
        self.assertTrue(validar_cpf("52998224725"))

    def test_validar_cpf_digitos_repetidos(self):
        # Bug conhecido: CPF com todos os dígitos iguais passa na validação
        self.assertFalse(validar_cpf("111.111.111-11"))

    def test_validar_cpf_tamanho_invalido(self):
        self.assertFalse(validar_cpf("123456789"))

    def test_validar_cpf_vazio(self):
        self.assertFalse(validar_cpf(""))

    def test_validar_cpf_none(self):
        self.assertFalse(validar_cpf(None))

    def test_extrair_digitos(self):
        self.assertEqual(
            extrair_digitos("529.982.247-25"),
            [5, 2, 9, 9, 8, 2, 2, 4, 7, 2, 5],
        )

    def test_formatar_cpf(self):
        self.assertEqual(formatar_cpf("52998224725"), "529.982.247-25")

    def test_mascarar_cpf(self):
        self.assertEqual(mascarar_cpf("529.982.247-25"), "***.***.***-25")

    def test_gerar_cpf_valido(self):
        cpf = gerar_cpf()
        self.assertTrue(validar_cpf(cpf))

    def test_gerar_cpf_tamanho(self):
        self.assertEqual(len(gerar_cpf()), 11)


if __name__ == "__main__":
    unittest.main()