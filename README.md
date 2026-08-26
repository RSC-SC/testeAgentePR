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
v.validar_cpf("123.456.789-09")     # True
```

### 4. Conversão de Unidades (`converter.py`)

Módulo para conversão entre diferentes unidades de medida.

```python
from converter import UnitConverter

c = UnitConverter()
c.comprimento(1, "km", "m")      # 1000.0
c.temperatura(100, "C", "F")     # 212.0
```

### 5. Utilitários de Strings (`string_utils.py`)

Módulo com funções úteis para manipulação de strings.

```python
from string_utils import StringUtils

s = StringUtils()
s.para_camel_case("meu nome")  # MeuNome
s.remover_acentos("café")      # cafe
```

### 6. Geração de Dados Falsos (`fake_data.py`)

Módulo para gerar dados falsos realistas para testes.

```python
from fake_data import FakeData

fake = FakeData()

# Nomes
fake.nome()                    # "Maria Silva Santos"

# Documentos
fake.cpf()                     # "123.456.789-09"
fake.cnpj()                    # "11.222.333/0001-81"

# Contato
fake.email()                   # "maria.santos@gmail.com"
fake.telefone()                # "(11) 99999-9999"

# Endereço
fake.endereco()                # "Rua das Flores, 123 - Centro, São Paulo - SP, 01234-567"

# Data e Hora
fake.data_formatada()          # "15/03/2026"
fake.hora()                    # "14:30"

# Empresa
fake.empresa()                 # "Tech Solutions"
fake.preco()                   # "R$ 1.234,56"

# Cartão de Crédito
fake.numero_cartao()           # "1234 5678 9012 3456"
fake.validade_cartao()         # "12/28"

# Pessoa completa
fake.pessoa()                  # {'nome': '...', 'cpf': '...', 'email': '...', ...}
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
├── test_date_handler.py   # Testes do date_handler
├── test_validator.py      # Testes do validator
├── test_converter.py      # Testes do converter
├── test_string_utils.py   # Testes do string_utils
└── test_fake_data.py      # Testes do fake_data
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
pytest test_fake_data.py -v
```

## Funcionalidades do FakeData

### Nomes

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `nome()` | Nome completo | "Maria Silva Santos" |
| `primeiro_nome()` | Apenas primeiro nome | "Maria" |
| `sobrenome()` | Apenas sobrenome | "Silva" |

### Documentos

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `cpf()` | CPF válido | "123.456.789-09" |
| `cnpj()` | CNPJ válido | "11.222.333/0001-81" |

### Contato

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `email()` | Email | "maria@gmail.com" |
| `telefone()` | Telefone fixo | "(11) 3456-7890" |
| `celular()` | Celular | "(11) 99999-9999" |

### Endereço

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `endereco()` | Endereço completo | "Rua das Flores, 123..." |
| `cep()` | CEP | "01234-567" |
| `cidade()` | Cidade | "São Paulo" |
| `estado()` | Estado | "SP" |

### Empresa

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `empresa()` | Nome da empresa | "Tech Solutions" |
| `cnpj()` | CNPJ | "11.222.333/0001-81" |
| `preco()` | Preço formatado | "R$ 1.234,56" |

### Cartão

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `numero_cartao()` | Número válido | "1234 5678 9012 3456" |
| `validade_cartao()` | Validade | "12/28" |
| `cvv()` | CVV | "123" |

## Licença

MIT