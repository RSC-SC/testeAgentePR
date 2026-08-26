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
handler.adicionar_dias(7)
print(handler.eh_fim_de_semana()) # False
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

# Comprimento
print(c.comprimento(1, "km", "m"))      # 1000.0
print(c.comprimento(12, "in", "cm"))    # 30.48

# Massa
print(c.massa(1, "kg", "g"))            # 1000.0
print(c.massa(1, "lb", "kg"))           # 0.453592

# Temperatura
print(c.temperatura(100, "C", "F"))     # 212.0
print(c.temperatura(32, "F", "C"))      # 0.0

# Volume
print(c.volume(1, "gal", "L"))          # 3.78541

# Velocidade
print(c.velocidade(100, "km/h", "m/s")) # 27.7778
```

## Estrutura do Projeto

```
testeAgentePR/
├── README.md              # Este arquivo
├── calculator.py          # Módulo de calculadora
├── date_handler.py        # Módulo de manipulação de datas
├── validator.py           # Módulo de validação
├── converter.py           # Módulo de conversão de unidades
├── test_date_handler.py   # Testes do date_handler
├── test_validator.py      # Testes do validator
└── test_converter.py      # Testes do converter
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
pytest test_converter.py -v
```

## Unidades Suportadas

### Comprimento
| Código | Nome |
|--------|------|
| m | metro |
| km | quilômetro |
| cm | centímetro |
| mm | milímetro |
| ft | pé |
| in | polegada |
| mi | milha |
| yd | jarda |

### Massa
| Código | Nome |
|--------|------|
| kg | quilograma |
| g | grama |
| mg | miligrama |
| lb | libra |
| oz | onça |
| t | tonelada |

### Temperatura
| Código | Nome |
|--------|------|
| C | Celsius |
| F | Fahrenheit |
| K | Kelvin |

### Volume
| Código | Nome |
|--------|------|
| L | litro |
| mL | mililitro |
| gal | galão |
| cup | xícara |
| fl_oz | onça fluida |

### Velocidade
| Código | Nome |
|--------|------|
| km/h | quilômetro por hora |
| m/s | metro por segundo |
| mph | milha por hora |
| kn | nó |

## Licença

MIT