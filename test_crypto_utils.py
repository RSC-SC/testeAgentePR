"""
Testes unitários para o módulo CryptoUtils
"""

import pytest
from crypto_utils import CryptoUtils


class TestCryptoUtils:
    """Testes para a classe CryptoUtils."""
    
    def setup_method(self):
        """Configuração antes de cada teste."""
        self.crypto = CryptoUtils()
    
    # ========== HASH ==========
    
    def test_md5(self):
        """Testa cálculo de MD5."""
        # MD5 de "hello" é conhecido
        assert self.crypto.md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    
    def test_md5_vazio(self):
        """Testa MD5 de string vazia."""
        assert self.crypto.md5("") == "d41d8cd98f00b204e9800998ecf8427e"
    
    def test_sha1(self):
        """Testa cálculo de SHA-1."""
        resultado = self.crypto.sha1("hello")
        assert len(resultado) == 40
        assert all(c in '0123456789abcdef' for c in resultado)
    
    def test_sha256(self):
        """Testa cálculo de SHA-256."""
        resultado = self.crypto.sha256("hello")
        assert len(resultado) == 64
    
    def test_sha512(self):
        """Testa cálculo de SHA-512."""
        resultado = self.crypto.sha512("hello")
        assert len(resultado) == 128
    
    def test_hash_consistencia(self):
        """Testa se mesmo input gera mesmo hash."""
        texto = "test"
        assert self.crypto.md5(texto) == self.crypto.md5(texto)
        assert self.crypto.sha256(texto) == self.crypto.sha256(texto)
    
    def test_hash_diferente_input(self):
        """Testa se inputs diferentes geram hashes diferentes."""
        assert self.crypto.md5("hello") != self.crypto.md5("world")
        assert self.crypto.sha256("hello") != self.crypto.sha256("world")
    
    # ========== HMAC ==========
    
    def test_hmac_sha256(self):
        """Testa cálculo de HMAC-SHA256."""
        resultado = self.crypto.hmac_sha256("mensagem", "chave")
        assert len(resultado) == 64
    
    def test_hmac_sha512(self):
        """Testa cálculo de HMAC-SHA512."""
        resultado = self.crypto.hmac_sha512("mensagem", "chave")
        assert len(resultado) == 128
    
    def test_verificar_hmac(self):
        """Testa verificação de HMAC."""
        mensagem = "teste"
        chave = "secreta"
        hmac_val = self.crypto.hmac_sha256(mensagem, chave)
        
        assert self.crypto.verificar_hmac(mensagem, chave, hmac_val) is True
    
    def test_verificar_hmac_invalido(self):
        """Testa verificação de HMAC inválido."""
        assert self.crypto.verificar_hmac("teste", "chave", "hmac_invalido") is False
    
    def test_hmac_sensivel_chave(self):
        """Testa se HMAC muda com chave diferente."""
        mensagem = "teste"
        hmac1 = self.crypto.hmac_sha256(mensagem, "chave1")
        hmac2 = self.crypto.hmac_sha256(mensagem, "chave2")
        assert hmac1 != hmac2
    
    # ========== BASE64 ==========
    
    def test_base64_encode_decode(self):
        """Testa encode e decode de Base64."""
        texto = "Hello World!"
        codificado = self.crypto.base64_encode(texto)
        decodificado = self.crypto.base64_decode(codificado)
        
        assert decodificado == texto
    
    def test_base64_encode(self):
        """Testa encode de Base64."""
        resultado = self.crypto.base64_encode("hello")
        assert resultado == "aGVsbG8="
    
    def test_base64_url_encode_decode(self):
        """Testa encode e decode de Base64 URL-safe."""
        texto = "https://example.com/path?q=1&b=2"
        codificado = self.crypto.base64_url_encode(texto)
        decodificado = self.crypto.base64_url_decode(codificado)
        
        assert decodificado == texto
    
    # ========== TOKENS ==========
    
    def test_gerar_token(self):
        """Testa geração de token."""
        token = self.crypto.gerar_token(16)
        assert len(token) == 16
        assert all(c in '0123456789abcdef' for c in token)
    
    def test_gerar_token_url_safe(self):
        """Testa geração de token URL-safe."""
        token = self.crypto.gerar_token_url_safe(16)
        assert len(token) > 0
    
    def test_gerar_token_alfanumerico(self):
        """Testa geração de token alfanumérico."""
        token = self.crypto.gerar_token_alfanumerico(16)
        assert len(token) == 16
        assert token.isalnum()
    
    def test_gerar_uuid(self):
        """Testa geração de UUID."""
        uuid = self.crypto.gerar_uuid()
        assert len(uuid) == 36  # Formato xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        assert uuid.count('-') == 4
    
    def test_tokens_unicos(self):
        """Testa se tokens gerados são únicos."""
        tokens = [self.crypto.gerar_token(16) for _ in range(100)]
        assert len(set(tokens)) == 100
    
    # ========== SENHAS ==========
    
    def test_gerar_senha_simples(self):
        """Testa geração de senha simples."""
        senha = self.crypto.gerar_senha(12, complexa=False)
        assert len(senha) == 12
        assert all(c.isalnum() for c in senha)
    
    def test_gerar_senha_complexa(self):
        """Testa geração de senha complexa."""
        senha = self.crypto.gerar_senha(16)
        assert len(senha) == 16
        # Deve ter pelo menos um de cada tipo
        assert any(c.isupper() for c in senha)
        assert any(c.islower() for c in senha)
        assert any(c.isdigit() for c in senha)
        assert any(c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for c in senha)
    
    def test_gerar_pin(self):
        """Testa geração de PIN."""
        pin = self.crypto.gerar_pin(6)
        assert len(pin) == 6
        assert pin.isdigit()
    
    def test_validar_fortaleza_senha_forte(self):
        """Testa validação de senha forte."""
        resultado = self.crypto.validar_fortaleza_senha("MinhaSenh@123")
        assert resultado["nivel"] == "forte"
        assert resultado["tem_maiuscula"] is True
        assert resultado["tem_minuscula"] is True
        assert resultado["tem_digito"] is True
        assert resultado["tem_especial"] is True
    
    def test_validar_fortaleza_senha_fraca(self):
        """Testa validação de senha fraca."""
        resultado = self.crypto.validar_fortaleza_senha("123")
        assert resultado["nivel"] == "fraca"
    
    # ========== XOR ==========
    
    def test_xor_criptografar_descriptografar(self):
        """Testa criptografia e descriptografia XOR."""
        original = "Hello World!"
        chave = "secret"
        
        criptografado = self.crypto.xor_criptografar(original, chave)
        descriptografado = self.crypto.xor_descriptografar(criptografado, chave)
        
        assert descriptografado == original
    
    def test_xor_resultado_hex(self):
        """Testa se XOR retorna hexadecimal."""
        resultado = self.crypto.xor_criptografar("hello", "key")
        assert all(c in '0123456789abcdef' for c in resultado)
    
    # ========== CIFRA DE CÉSAR ==========
    
    def test_cesar_criptografar(self):
        """Testa criptografia de César."""
        resultado = self.crypto.cesar_criptografar("ABC", 3)
        assert resultado == "DEF"
    
    def test_cesar_descriptografar(self):
        """Testa descriptografia de César."""
        resultado = self.crypto.cesar_descriptografar("DEF", 3)
        assert resultado == "ABC"
    
    def test_cesar_ciclico(self):
        """Testa se César é cíclico."""
        # Z + 1 deve voltar para A
        resultado = self.crypto.cesar_criptografar("Z", 1)
        assert resultado == "A"
    
    def test_cesar_mantem_nao_alfabeticos(self):
        """Testa se César mantém caracteres não alfabéticos."""
        resultado = self.crypto.cesar_criptografar("Hello, World!", 3)
        assert " " in resultado
        assert "," in resultado
        assert "!" in resultado
    
    # ========== TRANSPOSIÇÃO ==========
    
    def test_base_transposicao(self):
        """Testa transposição de colunas."""
        resultado = self.crypto.base_transposicao("HELLO", 3)
        # HEO -> L,L
        assert len(resultado) == 5


class TestFuncoesAuxiliares:
    """Testes para funções auxiliares."""
    
    def test_md5(self):
        """Testa função md5."""
        from crypto_utils import md5
        assert md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    
    def test_sha256(self):
        """Testa função sha256."""
        from crypto_utils import sha256
        assert len(sha256("hello")) == 64
    
    def test_base64_encode_decode(self):
        """Testa funções base64."""
        from crypto_utils import base64_encode, base64_decode
        texto = "test"
        assert base64_decode(base64_encode(texto)) == texto
    
    def test_gerar_token(self):
        """Testa função gerar_token."""
        from crypto_utils import gerar_token
        assert len(gerar_token(16)) == 16
    
    def test_gerar_senha(self):
        """Testa função gerar_senha."""
        from crypto_utils import gerar_senha
        assert len(gerar_senha(12)) == 12


class TestReprodutibilidade:
    """Testes para verificar comportamento determinístico."""
    
    def test_hash_deterministico(self):
        """Testa se hash é determinístico."""
        crypto = CryptoUtils()
        texto = "deterministico"
        
        # Múltiplas chamadas devem retornar o mesmo resultado
        for _ in range(10):
            assert crypto.md5(texto) == "5d41402abc4b2a76b9719d911017c592"
    
    def test_hmac_deterministico(self):
        """Testa se HMAC é determinístico."""
        crypto = CryptoUtils()
        mensagem = "teste"
        chave = "chave"
        
        hmac1 = crypto.hmac_sha256(mensagem, chave)
        hmac2 = crypto.hmac_sha256(mensagem, chave)
        
        assert hmac1 == hmac2


class TestSeguranca:
    """Testes de segurança básica."""
    
    def test_tokens_nao_repetem(self):
        """Testa se tokens não se repetem em muitas gerações."""
        crypto = CryptoUtils()
        tokens = set()
        
        for _ in range(1000):
            token = crypto.gerar_token(32)
            tokens.add(token)
        
        # Em 1000 gerações, todos devem ser únicos
        assert len(tokens) == 1000
    
    def test_senhas_variadas(self):
        """Testa se senhas geradas são variadas."""
        crypto = CryptoUtils()
        senhas = set()
        
        for _ in range(100):
            senha = crypto.gerar_senha(16)
            senhas.add(senha)
        
        # A maioria das senhas deve ser única
        assert len(senhas) > 90


if __name__ == "__main__":
    pytest.main([__file__, "-v"])