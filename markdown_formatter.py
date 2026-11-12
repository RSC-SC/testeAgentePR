from typing import List, Optional


def format_heading(text: str, level: int = 1) -> str:
    """Gera um cabeçalho Markdown com nível de 1 a 6."""
    if level < 1:
        level = 1
    elif level > 6:
        level = 6
    hashes = "#" * level
    return f"{hashes} {text.strip()}"


def format_bullet_list(items: List[str], prefix: str = "-") -> str:
    """Gera uma lista com marcadores a partir de uma lista de itens."""
    if not items:
        return ""

    result = ""
    # Potencial melhoria: usar '\n'.join(...) em vez de concatenar string repetidamente
    for item in items:
        if item is not None and str(item).strip():
            result += f"{prefix} {str(item).strip()}\n"
    return result.rstrip()


def format_blockquote(text: str) -> str:
    """Formata um bloco de citação (blockquote) em Markdown."""
    if not text:
        return ""
    lines = text.strip().split("\n")
    return "\n".join(f"> {line}" for line in lines)
