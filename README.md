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
handler.adicionar_dias(7)
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

# Conversão
s.para_camel_case("meu nome eh joao")  # MeuNomeEhJoao
s.para_snake_case("MeuNomeVariavel")   # meu_nome_variavel

# Limpeza
s.remover_acentos("café")              # cafe
s.remover_espacos_extras("  hello   world  ")  # hello world

# Validação
s.eh_email("test@email.com")           # True
s.contem_apenas_letras("hello")        # True

# Extração
s.extrair_numeros("teste123abc456")    # ['123', '456']
s.extrair_emails("a@b.com e c@d.org") # ['a@b.com', 'c@d.org']

# Formatação
s.truncar("hello world", 5)            # hello...
s.inverter("hello")                    # olleh

# Análise
s.contar_vogais("hello")               # 2
s.frequencia_caracteres("hello")       # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
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
├── test_date_handler.py   # Testes do date_handler
├── test_validator.py      # Testes do validator
├── test_converter.py      # Testes do converter
└── test_string_utils.py   # Testes do string_utils
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
pytest test_string_utils.py -v
```

## Funcionalidades do StringUtils

### Conversão

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `para_maiusculas()` | Converte para maiúsculas | "hello" → "HELLO" |
| `para_minusculas()` | Converte para minúsculas | "HELLO" → "hello" |
| `para_titulo()` | Converte para título | "hello world" → "Hello World" |
| `para_camel_case()` | Converte para CamelCase | "hello world" → "HelloWorld" |
| `para_snake_case()` | Converte para snake_case | "HelloWorld" → "hello_world" |
| `para_kebab_case()` | Converte para kebab-case | "HelloWorld" → "hello-world" |

### Limpeza

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `remover_acentos()` | Remove acentos | "café" → "cafe" |
| `remover_espacos_extras()` | Remove espaços extras | "  hello  " → "hello" |
| `remover_numeros()` | Remove números | "teste123" → "teste" |
| `remover_especiais()` | Remove caracteres especiais | "hello!" → "hello" |

### Validação

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `contem_apenas_letras()` | Verifica se são apenas letras | "hello" → True |
| `contem_apenas_numeros()` | Verifica se são apenas números | "123" → True |
| `eh_email()` | Valida email | "a@b.com" → True |

### Extração

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `extrair_numeros()` | Extrai números | "a1b2" → ["1", "2"] |
| `extrair_emails()` | Extrai emails | "a@b.com" → ["a@b.com"] |
| `extrair_urls()` | Extrai URLs | "https://a.com" → ["https://a.com"] |

## Licença

MIT