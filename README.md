# testeAgentePR

Repositório de testes para o Agente Revisor de PRs.

## Funcionalidades

### 1. Calculadora Simples (`calculator.py`)

Módulo com operações matemáticas básicas.

```python
from calculator import somar, subtrair, multiplicar, dividir

print(somar(2, 3))        # 5
print(subtrair(10, 4))    # 6
print(multiplicar(5, 5))  # 25
print(dividir(10, 2))     # 5.0
```

### 2. Manipulação de Datas (`date_handler.py`)

Classe para operações comuns com datas.

```python
from date_handler import DateHandler

handler = DateHandler()
print(handler.data_atual())      # 25/08/2026
print(handler.dia_da_semana())    # Segunda-feira
handler.adicionar_dias(7)         # Adiciona 7 dias
print(handler.eh_fim_de_semana()) # False
```

### 3. Validação de Dados (`validator.py`)

Módulo completo para validação de diferentes tipos de dados.

```python
from validator import Validator

v = Validator()

# Validação de email
v.validar_email("user@example.com")  # True

# Validação de CPF
v.validar_cpf("123.456.789-09")  # True

# Validação de senha
valido, requisitos = v.validar_senha("MinhaSenh@123")
print(valido)  # True
print(requisitos)  # ['tamanho_minimo', 'maiuscula', 'minuscula', 'numero', 'especial']
```

## Estrutura do Projeto

```
testeAgentePR/
├── README.md              # Este arquivo
├── calculator.py          # Módulo de calculadora
├── date_handler.py        # Módulo de manipulação de datas
├── validator.py           # Módulo de validação
├── test_date_handler.py   # Testes do date_handler
└── test_validator.py      # Testes do validator
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
pytest test_date_handler.py -v
pytest test_validator.py -v
```

## Uso

### Calculadora

```python
from calculator import *

# Operações básicas
print(somar(10, 5))      # 15
print(potencia(2, 3))    # 8
print(raiz_quadrada(9))  # 3.0
```

### Datas

```python
from date_handler import DateHandler, parse_data

# Criar com data atual
handler = DateHandler()

# Criar com data específica
handler = DateHandler(datetime(2026, 12, 25))

# Parse de string
handler = parse_data("25/12/2026")
```

### Validação

```python
from validator import Validator

v = Validator()

# Validações individuais
v.validar_email("test@email.com")
v.validar_cpf("123.456.789-09")
v.validar_telefone("(11) 99999-9999")
v.validar_url("https://example.com")

# Verificar erros
if v.tem_erros():
    for erro in v.obter_erros():
        print(f"Erro: {erro['campo']} - {erro['mensagem']}")
```

## Licença

MIT