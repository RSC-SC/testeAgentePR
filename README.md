# testeAgentePR

Repositório de testes para o Agente Revisor de PRs.

## Funcionalidades

### Utilitários de Texto (`text_utils.py`)

Módulo com funções para normalização e processamento de texto.

```python
from text_utils import normalizar_texto, palavras_mais_frequentes, remover_acentos

print(normalizar_texto("  Olá   Mundo  "))   # "olá mundo"
print(palavras_mais_frequentes("a b a c a"))  # [('a', 3)]
print(remover_acentos("coração"))             # "coracao"
```

