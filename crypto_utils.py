"""
Módulo CryptoUtils - Utilitários de criptografia e hash

Este módulo fornece funções para hash, criptografia simples e geração de tokens.
"""

import hashlib
import hmac
import base64
import secrets
import string
from typing import Optional, Tuple


class CryptoUtils:
    """
    Classe com utilitários de criptografia e hash.
    
    Supports:
        - Hash: MD5, SHA-1, SHA-256, SHA-512
        - HMAC: Chave de autenticação
        - Base64: Codificação/decodificação
        - Tokens: Geração de tokens seguros
        - Senhas: Geração e validação
        - XOR: Criptografia simples
    
    Examples:
        >>> crypto = CryptoUtils()
        >>> crypto.md5("hello")
        '5d41402abc4b2a76b9719d911017c592'
        >>> crypto.gerar_token(16)
        'a1b2c3d4e5f6g7h8'
    """
    
    # ========== HASH ==========
    
    def md5(self, texto: str) -> str:
        """
        Calcula o hash MD5.
        
        Args:
            texto: Texto a ser hasheado
            
        Returns:
            Hash MD5 em hexadecimal
            
        Examples:
            >>> crypto = CryptoUtils()
            >>> crypto.md5("hello")
            '5d41402abc4b2a76b9719d911017c592'
        """
        return hashlib.md5(texto.encode()).hexdigest()
    
    def sha1(self, texto: str) -> str:
        """
        Calcula o hash SHA-1.
        
        Args:
            texto: Texto a ser hasheado
            
        Returns:
            Hash SHA-1 em hexadecimal
        """
        return hashlib.sha1(texto.encode()).hexdigest()
    
    def sha256(self, texto: str) -> str:
        """
        Calcula o hash SHA-256.
        
        Args:
            texto: Texto a ser hasheado
            
        Returns:
            Hash SHA-256 em hexadecimal
        """
        return hashlib.sha256(texto.encode()).hexdigest()
    
    def sha512(self, texto: str) -> str:
        """
        Calcula o hash SHA-512.
        
        Args:
            texto: Texto a ser hasheado
            
        Returns:
            Hash SHA-512 em hexadecimal
        """
        return hashlib.sha512(texto.encode()).hexdigest()
    
    def hash_arquivo(self, caminho: str, algoritmo: str = "sha256") -> str:
        """
        Calcula o hash de um arquivo.
        
        Args:
            caminho: Caminho do arquivo
            algoritmo: Algoritmo a ser usado (md5, sha1, sha256, sha512)
            
        Returns:
            Hash do arquivo em hexadecimal
        """
        hash_obj = hashlib.new(algoritmo)
        
        with open(caminho, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    
    # ========== HMAC ==========
    
    def hmac_sha256(self, mensagem: str, chave: str) -> str:
        """
        Calcula HMAC-SHA256.
        
        Args:
            mensagem: Mensagem a ser autenticada
            chave: Chave secreta
            
        Returns:
            HMAC em hexadecimal
            
        Examples:
            >>> crypto = CryptoUtils()
            >>> crypto.hmac_sha256("hello", "secret")
            '...'
        """
        return hmac.new(
            chave.encode(),
            mensagem.encode(),
            hashlib.sha256
        ).hexdigest()
    
    def hmac_sha512(self, mensagem: str, chave: str) -> str:
        """
        Calcula HMAC-SHA512.
        
        Args:
            mensagem: Mensagem a ser autenticada
            chave: Chave secreta
            
        Returns:
            HMAC em hexadecimal
        """
        return hmac.new(
            chave.encode(),
            mensagem.encode(),
            hashlib.sha512
        ).hexdigest()
    
    def verificar_hmac(self, mensagem: str, chave: str, hmac_esperado: str) -> bool:
        """
        Verifica se um HMAC é válido.
        
        Args:
            mensagem: Mensagem original
            chave: Chave secreta
            hmac_esperado: HMAC a ser verificado
            
        Returns:
            True se o HMAC for válido
        """
        hmac_calculado = self.hmac_sha256(mensagem, chave)
        return hmac.compare_digest(hmac_calculado, hmac_esperado)
    
    # ========== BASE64 ==========
    
    def base64_encode(self, texto: str) -> str:
        """
        Codifica texto em Base64.
        
        Args:
            texto: Texto a ser codificado
            
        Returns:
            Texto codificado em Base64
            
        Examples:
            >>> crypto = CryptoUtils()
            >>> crypto.base64_encode("hello")
            'aGVsbG8='
        """
        return base64.b64encode(texto.encode()).decode()
    
    def base64_decode(self, texto_codificado: str) -> str:
        """
        Decodifica texto de Base64.
        
        Args:
            texto_codificado: Texto codificado
            
        Returns:
            Texto original
        """
        return base64.b64decode(texto_codificado.encode()).decode()
    
    def base64_url_encode(self, texto: str) -> str:
        """
        Codifica texto em Base64 URL-safe.
        
        Args:
            texto: Texto a ser codificado
            
        Returns:
            Texto codificado em Base64 URL-safe
        """
        return base64.urlsafe_b64encode(texto.encode()).decode()
    
    def base64_url_decode(self, texto_codificado: str) -> str:
        """
        Decodifica texto de Base64 URL-safe.
        
        Args:
            texto_codificado: Texto codificado
            
        Returns:
            Texto original
        """
        return base64.urlsafe_b64decode(texto_codificado.encode()).decode()
    
    # ========== TOKENS ==========
    
    def gerar_token(self, tamanho: int = 32) -> str:
        """
        Gera um token aleatório seguro.
        
        Args:
            tamanho: Tamanho do token em caracteres
            
        Returns:
            Token hexadecimal
            
        Examples:
            >>> crypto = CryptoUtils()
            >>> crypto.gerar_token(16)
            'a1b2c3d4e5f67890'
        """
        return secrets.token_hex(tamanho // 2)
    
    def gerar_token_url_safe(self, tamanho: int = 32) -> str:
        """
        Gera um token URL-safe.
        
        Args:
            tamanho: Tamanho do token em bytes
            
        Returns:
            Token URL-safe
        """
        return secrets.token_urlsafe(tamanho)
    
    def gerar_token_alfanumerico(self, tamanho: int = 32) -> str:
        """
        Gera um token alfanumérico.
        
        Args:
            tamanho: Tamanho do token
            
        Returns:
            Token alfanumérico
        """
        caracteres = string.ascii_letters + string.digits
        return ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    
    def gerar_uuid(self) -> str:
        """
        Gera um UUID v4.
        
        Returns:
            UUID formatado
        """
        return str(secrets.token_uuid4())
    
    # ========== SENHAS ==========
    
    def gerar_senha(self, tamanho: int = 16, complexa: bool = True) -> str:
        """
        Gera uma senha segura.
        
        Args:
            tamanho: Tamanho da senha
            complexa: Se deve incluir todos os tipos de caracteres
            
        Returns:
            Senha gerada
            
        Examples:
            >>> crypto = CryptoUtils()
            >>> crypto.gerar_senha(12)
            'Kj8#mN2$pL5q'
        """
        if complexa:
            caracteres = (
                string.ascii_letters +
                string.digits +
                string.punctuation
            )
        else:
            caracteres = string.ascii_letters + string.digits
        
        # Garante pelo menos um de cada tipo se for complexa
        if complexa and tamanho >= 4:
            senha = [
                secrets.choice(string.ascii_uppercase),
                secrets.choice(string.ascii_lowercase),
                secrets.choice(string.digits),
                secrets.choice(string.punctuation),
            ]
            senha += [secrets.choice(caracteres) for _ in range(tamanho - 4)]
            secrets.SystemRandom().shuffle(senha)
            return ''.join(senha)
        
        return ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    
    def gerar_pin(self, tamanho: int = 6) -> str:
        """
        Gera um PIN numérico.
        
        Args:
            tamanho: Tamanho do PIN
            
        Returns:
            PIN numérico
        """
        return ''.join(secrets.choice(string.digits) for _ in range(tamanho))
    
    def validar_fortaleza_senha(self, senha: str) -> dict:
        """
        Valida a fortaleza de uma senha.
        
        Args:
            senha: Senha a ser validada
            
        Returns:
            Dicionário com análise da senha
        """
        resultado = {
            "tamanho": len(senha),
            "tem_maiuscula": any(c.isupper() for c in senha),
            "tem_minuscula": any(c.islower() for c in senha),
            "tem_digito": any(c.isdigit() for c in senha),
            "tem_especial": any(c in string.punctuation for c in senha),
            "pontuacao": 0,
            "nivel": ""
        }
        
        # Calcula pontuação
        pontos = 0
        if resultado["tamanho"] >= 8:
            pontos += 1
        if resultado["tamanho"] >= 12:
            pontos += 1
        if resultado["tem_maiuscula"]:
            pontos += 1
        if resultado["tem_minuscula"]:
            pontos += 1
        if resultado["tem_digito"]:
            pontos += 1
        if resultado["tem_especial"]:
            pontos += 1
        
        resultado["pontuacao"] = pontos
        
        # Define nível
        if pontos <= 2:
            resultado["nivel"] = "fraca"
        elif pontos <= 4:
            resultado["nivel"] = "media"
        else:
            resultado["nivel"] = "forte"
        
        return resultado
    
    # ========== XOR ==========
    
    def xor_criptografar(self, texto: str, chave: str) -> str:
        """
        Criptografa texto usando XOR.
        
        Args:
            texto: Texto a ser criptografado
            chave: Chave de criptografia
            
        Returns:
            Texto criptografado em hexadecimal
            
        Examples:
            >>> crypto = CryptoUtils()
            >>> crypto.xor_criptografar("hello", "key")
            '...'
        """
        texto_bytes = texto.encode()
        chave_bytes = chave.encode()
        
        # Repete a chave para cobrir todo o texto
        chave_repetida = (chave_bytes * (len(texto_bytes) // len(chave_bytes) + 1))[:len(texto_bytes)]
        
        # Aplica XOR
        resultado = bytes(a ^ b for a, b in zip(texto_bytes, chave_repetida))
        
        return resultado.hex()
    
    def xor_descriptografar(self, texto_criptografado: str, chave: str) -> str:
        """
        Descriptografa texto XOR.
        
        Args:
            texto_criptografado: Texto em hexadecimal
            chave: Chave de criptografia
            
        Returns:
            Texto original
        """
        texto_bytes = bytes.fromhex(texto_criptografado)
        chave_bytes = chave.encode()
        
        # Repete a chave
        chave_repetida = (chave_bytes * (len(texto_bytes) // len(chave_bytes) + 1))[:len(texto_bytes)]
        
        # Aplica XOR (mesma operação)
        resultado = bytes(a ^ b for a, b in zip(texto_bytes, chave_repetida))
        
        return resultado.decode()
    
    # ========== CIPHER SIMPLES ==========
    
    def cesar_criptografar(self, texto: str, deslocamento: int = 3) -> str:
        """
        Criptografa usando cifra de César.
        
        Args:
            texto: Texto a ser criptografado
            deslocamento: Número de posições para deslocar
            
        Returns:
            Texto criptografado
        """
        resultado = []
        
        for char in texto:
            if char.isalpha():
                ascii_base = ord('A') if char.isupper() else ord('a')
                char_criptografado = chr((ord(char) - ascii_base + deslocamento) % 26 + ascii_base)
                resultado.append(char_criptografado)
            else:
                resultado.append(char)
        
        return ''.join(resultado)
    
    def cesar_descriptografar(self, texto: str, deslocamento: int = 3) -> str:
        """
        Descriptografa cifra de César.
        
        Args:
            texto: Texto criptografado
            deslocamento: Número de posições deslocadas
            
        Returns:
            Texto original
        """
        return self.cesar_criptografar(texto, -deslocamento)
    
    def base_transposicao(self, texto: str, chave: int = 3) -> str:
        """
        Criptografa usando transposição de colunas.
        
        Args:
            texto: Texto a ser criptografado
            chave: Número de colunas
            
        Returns:
            Texto criptografado
        """
        # Remove espaços
        texto = texto.replace(" ", "")
        
        # Cria grade
        grade = [''] * chave
        for i, char in enumerate(texto):
            grade[i % chave] += char
        
        return ''.join(grade)


# Funções auxiliares para uso rápido
def md5(texto: str) -> str:
    """Calcula MD5."""
    return CryptoUtils().md5(texto)

def sha256(texto: str) -> str:
    """Calcula SHA-256."""
    return CryptoUtils().sha256(texto)

def base64_encode(texto: str) -> str:
    """Codifica em Base64."""
    return CryptoUtils().base64_encode(texto)

def base64_decode(texto: str) -> str:
    """Decodifica Base64."""
    return CryptoUtils().base64_decode(texto)

def gerar_token(tamanho: int = 32) -> str:
    """Gera um token."""
    return CryptoUtils().gerar_token(tamanho)

def gerar_senha(tamanho: int = 16) -> str:
    """Gera uma senha."""
    return CryptoUtils().gerar_senha(tamanho)


# Função principal para demonstração
if __name__ == "__main__":
    print("=== CryptoUtils - Utilitários de Criptografia ===\n")
    
    crypto = CryptoUtils()
    
    # Hash
    print("🔒 Hash:")
    print(f"  MD5: {crypto.md5('hello')}")
    print(f"  SHA-1: {crypto.sha1('hello')[:40]}...")
    print(f"  SHA-256: {crypto.sha256('hello')[:40]}...")
    print(f"  SHA-512: {crypto.sha512('hello')[:40]}...")
    
    # HMAC
    print("\n🔑 HMAC:")
    hmac_val = crypto.hmac_sha256("mensagem", "chave_secreta")
    print(f"  HMAC-SHA256: {hmac_val[:40]}...")
    print(f"  Verificação: {crypto.verificar_hmac('mensagem', 'chave_secreta', hmac_val)}")
    
    # Base64
    print("\n📦 Base64:")
    codificado = crypto.base64_encode("Hello World!")
    print(f"  Encode: {codificado}")
    print(f"  Decode: {crypto.base64_decode(codificado)}")
    
    # Tokens
    print("\n🎫 Tokens:")
    print(f"  Token Hex: {crypto.gerar_token(16)}")
    print(f"  Token URL: {crypto.gerar_token_url_safe(16)}")
    print(f"  Token Alpha: {crypto.gerar_token_alfanumerico(16)}")
    print(f"  UUID: {crypto.gerar_uuid()}")
    
    # Senhas
    print("\n🔐 Senhas:")
    print(f"  Senha simples: {crypto.gerar_senha(12, complexa=False)}")
    print(f"  Senha complexa: {crypto.gerar_senha(16)}")
    print(f"  PIN: {crypto.gerar_pin(6)}")
    
    # Validação de senha
    senha = "MinhaSenh@123"
    resultado = crypto.validar_fortaleza_senha(senha)
    print(f"\n  Análise de '{senha}':")
    print(f"    Tamanho: {resultado['tamanho']}")
    print(f"    Maiúscula: {resultado['tem_maiuscula']}")
    print(f"    Minúscula: {resultado['tem_minuscula']}")
    print(f"    Dígito: {resultado['tem_digito']}")
    print(f"    Especial: {resultado['tem_especial']}")
    print(f"    Nível: {resultado['nivel']}")
    
    # XOR
    print("\n🔐 XOR:")
    original = "Hello World!"
    chave = "secret"
    criptografado = crypto.xor_criptografar(original, chave)
    descriptografado = crypto.xor_descriptografar(criptografado, chave)
    print(f"  Original: {original}")
    print(f"  Criptografado: {criptografado}")
    print(f"  Descriptografado: {descriptografado}")
    
    # Cifra de César
    print("\n📜 Cifra de César:")
    original = "Hello World!"
    criptografado = crypto.cesar_criptografar(original, 3)
    descriptografado = crypto.cesar_descriptografar(criptografado, 3)
    print(f"  Original: {original}")
    print(f"  Criptografado (+3): {criptografado}")
    print(f"  Descriptografado: {descriptografado}")