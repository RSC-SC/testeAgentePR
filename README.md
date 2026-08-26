# testeAgentePR

Repositório de testes para o Agente Revisor de PRs.

## Funcionalidades

### 1. Calculadora Simples (`calculator.py`)

Módulo com operações matemáticas básicas.

```python
from calculator import somar, subtrair, multiplicar, dividir

print(somar(2, 3))        # 5
print(dividir(10, 2))     # 5.0
```

### 2. Manipulação de Datas (`date_handler.py`)

Classe para operações comuns com datas.

```python
from date_handler import DateHandler

handler = DateHandler()
print(handler.data_atual())      # 25/08/2026
```

### 3. Validação de Dados (`validator.py`)

Módulo completo para validação de diferentes tipos de dados.

```python
from validator import Validator

v = Validator()
v.validar_email("user@example.com")  # True
```

### 4. Conversão de Unidades (`converter.py`)

Módulo para conversão entre diferentes unidades de medida.

```python
from converter import UnitConverter

c = UnitConverter()
c.comprimento(1, "km", "m")      # 1000.0
```

### 5. Utilitários de Strings (`string_utils.py`)

Módulo com funções úteis para manipulação de strings.

```python
from string_utils import StringUtils

s = StringUtils()
s.para_camel_case("meu nome")  # MeuNome
```

### 6. Geração de Dados Falsos (`fake_data.py`)

Módulo para gerar dados falsos realistas para testes.

```python
from fake_data import FakeData

fake = FakeData()
fake.nome()    # "Maria Silva Santos"
fake.cpf()     # "123.456.789-09"
```

### 7. Utilitários de Criptografia (`crypto_utils.py`)

Módulo com funções de hash, criptografia e geração de tokens.

```python
from crypto_utils import CryptoUtils

crypto = CryptoUtils()

# Hash
crypto.md5("hello")           # "5d41402abc4b2a76b9719d911017c592"
crypto.sha256("hello")        # 64 caracteres

# HMAC
crypto.hmac_sha256("msg", "key")  # Autenticação

# Base64
crypto.base64_encode("hello")     # "aGVsbG8="
crypto.base64_decode("aGVsbG8=")  # "hello"

# Tokens
crypto.gerar_token(16)            # "a1b2c3d4e5f67890"
crypto.gerar_token_url_safe(16)   # Token URL-safe
crypto.gerar_uuid()               # UUID v4

# Senhas
crypto.gerar_senha(16)            # Senha complexa
crypto.gerar_pin(6)               # "123456"
crypto.validar_fortaleza_senha("MinhaSenh@123")

# Criptografia simples
crypto.xor_criptografar("hello", "key")    # XOR
crypto.cesar_criptografar("ABC", 3)        # "DEF"
```

## Estrutura do Projeto

```
testeAgentePR/
├── README.md              # Este arquivo
├── calculator.py          # Módulo de calculadora
├── date_handler.py        # Módulo de manipulação de datas
├── validator.py           # Módulo de validação
├── converter.py           # Módulo de conversão de unidades
├── string_utils.py        # Módulo de utilitários de strings
├── fake_data.py           # Módulo de geração de dados falsos
├── crypto_utils.py        # Módulo de criptografia
├── test_*.py              # Testes de cada módulo
```

## Instalação

```bash
git clone https://github.com/RSC-SC/testeAgentePR.git
cd testeAgentePR
```

## Testes

```bash
# Executar todos os testes
pytest

# Executar testes específicos
pytest test_crypto_utils.py -v
```

## Funcionalidades do CryptoUtils

### Hash

| Método | Descrição | Tamanho |
|--------|-----------|---------|
| `md5()` | Hash MD5 | 32 hex |
| `sha1()` | Hash SHA-1 | 40 hex |
| `sha256()` | Hash SHA-256 | 64 hex |
| `sha512()` | Hash SHA-512 | 128 hex |

### HMAC

| Método | Descrição |
|--------|-----------|
| `hmac_sha256()` | HMAC-SHA256 |
| `hmac_sha512()` | HMAC-SHA512 |
| `verificar_hmac()` | Verifica HMAC |

### Base64

| Método | Descrição |
|--------|-----------|
| `base64_encode()` | Codifica |
| `base64_decode()` | Decodifica |
| `base64_url_encode()` | URL-safe |

### Tokens

| Método | Descrição |
|--------|-----------|
| `gerar_token()` | Token hexadecimal |
| `gerar_token_url_safe()` | Token URL-safe |
| `gerar_token_alfanumerico()` | Token alfanumérico |
| `gerar_uuid()` | UUID v4 |

### Senhas

| Método | Descrição |
|--------|-----------|
| `gerar_senha()` | Senha segura |
| `gerar_pin()` | PIN numérico |
| `validar_fortaleza_senha()` | Analisa fortaleza |

### Criptografia

| Método | Descrição |
|--------|-----------|
| `xor_criptografar()` | XOR simples |
| `cesar_criptografar()` | Cifra de César |
| `base_transposicao()` | Transposição |

## Licença

MIT