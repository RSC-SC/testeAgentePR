"""
Testes unitários para o módulo Validator
"""

import pytest
from validator import Validator, ValidationError


class TestValidator:
    """Testes para a classe Validator."""
    
    def setup_method(self):
        """Configuração antes de cada teste."""
        self.v = Validator()
    
    # ========== EMAIL ==========
    
    def test_email_valido(self):
        """Testa email válido."""
        assert self.v.validar_email("user@example.com") is True
        assert self.v.validar_email("test.name@domain.co.uk") is True
    
    def test_email_invalido(self):
        """Testa email inválido."""
        assert self.v.validar_email("invalid-email") is False
        assert self.v.validar_email("@domain.com") is False
        assert self.v.validar_email("user@") is False
    
    # ========== CPF ==========
    
    def test_cpf_valido(self):
        """Testa CPF válido."""
        assert self.v.validar_cpf("123.456.789-09") is True
    
    def test_cpf_invalido(self):
        """Testa CPF inválido."""
        assert self.v.validar_cpf("111.111.111-11") is False
        assert self.v.validar_cpf("12345678901") is False  # Sem formatação mas inválido
    
    def test_cpf_tamanho_incorreto(self):
        """Testa CPF com tamanho incorreto."""
        assert self.v.validar_cpf("123.456.789-0") is False
        assert self.v.validar_cpf("123.456.789-090") is False
    
    # ========== CNPJ ==========
    
    def test_cnpj_valido(self):
        """Testa CNPJ válido."""
        assert self.v.validar_cnpj("11.222.333/0001-81") is True
    
    def test_cnpj_invalido(self):
        """Testa CNPJ inválido."""
        assert self.v.validar_cnpj("11.111.111/1111-11") is False
    
    # ========== TELEFONE ==========
    
    def test_telefone_valido(self):
        """Testa telefone válido."""
        assert self.v.validar_telefone("(11) 99999-9999") is True
        assert self.v.validar_telefone("11999999999") is True
    
    def test_telefone_invalido(self):
        """Testa telefone inválido."""
        assert self.v.validar_telefone("99999-9999") is False  # Sem DDD
        assert self.v.validar_telefone("123456789012") is False  # Muito longo
    
    # ========== SENHA ==========
    
    def test_senha_forte(self):
        """Testa senha forte."""
        valido, requisitos = self.v.validar_senha("MinhaSenh@123")
        assert valido is True
        assert len(requisitos) == 5
    
    def test_senha_fraca(self):
        """Testa senha fraca."""
        valido, requisitos = self.v.validar_senha("123")
        assert valido is False
        assert len(requisitos) < 5
    
    def test_senha_sem_maiuscula(self):
        """Testa senha sem letra maiúscula."""
        valido, requisitos = self.v.validar_senha("minha123@")
        assert "maiuscula" not in requisitos
    
    def test_senha_sem_especial(self):
        """Testa senha sem caractere especial."""
        valido, requisitos = self.v.validar_senha("MinhaSenha123")
        assert "especial" not in requisitos
    
    # ========== URL ==========
    
    def test_url_valida(self):
        """Testa URL válida."""
        assert self.v.validar_url("https://www.google.com") is True
        assert self.v.validar_url("http://example.com/path") is True
    
    def test_url_invalida(self):
        """Testa URL inválida."""
        assert self.v.validar_url("invalid-url") is False
        assert self.v.validar_url("ftp://files.com") is False
    
    # ========== NÚMERO ==========
    
    def test_numero_valido(self):
        """Testa número válido."""
        assert self.v.validar_numero(42) is True
        assert self.v.validar_numero("3.14") is True
    
    def test_numero_fora_limites(self):
        """Testa número fora dos limites."""
        assert self.v.validar_numero(5, minimo=10) is False
        assert self.v.validar_numero(15, maximo=10) is False
    
    def test_numero_invalido(self):
        """Testa valor não numérico."""
        assert self.v.validar_numero("abc") is False
    
    # ========== LISTA ==========
    
    def test_lista_nao_vazia(self):
        """Testa lista não vazia."""
        assert self.v.validar_lista_nao_vazia([1, 2, 3]) is True
    
    def test_lista_vazia(self):
        """Testa lista vazia."""
        assert self.v.validar_lista_nao_vazia([]) is False
    
    # ========== ERROS ==========
    
    def test_acumulo_erros(self):
        """Testa acumulo de erros."""
        self.v.validar_email("invalid")
        self.v.validar_cpf("123")
        
        assert self.v.tem_erros() is True
        assert len(self.v.obter_erros()) == 2
    
    def test_limpar_erros(self):
        """Testa limpeza de erros."""
        self.v.validar_email("invalid")
        self.v.limpar_erros()
        
        assert self.v.tem_erros() is False


class TestValidatorIntegration:
    """Testes de integração para o Validator."""
    
    def test_validacao_completa_usuario(self):
        """Testa validação completa de dados de usuário."""
        v = Validator()
        
        # Validações
        v.validar_email("user@example.com")
        v.validar_cpf("123.456.789-09")
        valido_senha, _ = v.validar_senha("MinhaSenh@123")
        
        # Resultado
        assert v.tem_erros() is False
        assert valido_senha is True
    
    def test_validacao_completa_com_erros(self):
        """Testa validação com múltiplos erros."""
        v = Validator()
        
        # Validações com erros
        v.validar_email("invalid")
        v.validar_cpf("111.111.111-11")
        v.validar_senha("123")
        
        # Resultado
        assert v.tem_erros() is True
        assert len(v.obter_erros()) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])