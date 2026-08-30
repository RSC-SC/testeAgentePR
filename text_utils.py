"""Módulo de utilitários para processamento e normalização de texto."""

import re
from collections import Counter


def normalizar_texto(texto):
    """Normaliza um texto: remove espaços extras e padroniza para minúsculas."""
    if not texto:
        return ""
    texto = texto.strip()
    texto = re.sub(r"\s+", " ", texto)
    return texto.lower()


def contar_palavras(texto):
    palavras = normalizar_texto(texto).split(" ")
    return len([p for p in palavras if p])


def palavras_mais_frequentes(texto, top_n=3):
    """Retorna as N palavras mais frequentes de um texto."""
    palavras = [p for p in normalizar_texto(texto).split(" ") if p]
    contagem = Counter(palavras)
    return contagem.most_common(top_n)


def remover_acentos(texto):
    """Remove acentos de um texto usando substituição manual."""
    mapa = {
        "á": "a", "à": "a", "â": "a", "ã": "a",
        "é": "e", "ê": "e",
        "í": "i",
        "ó": "o", "ô": "o", "õ": "o",
        "ú": "u",
        "ç": "c",
    }
    resultado = ""
    for char in texto:
        resultado += mapa.get(char, char)
    return resultado
