import re
from typing import Optional


def is_valid_url(url: str) -> bool:
    """Valida se uma string representa uma URL HTTP ou HTTPS válida."""
    if not url or not isinstance(url, str):
        return False

    pattern = re.compile(
        r"^https?://"  # http:// ou https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"  # domínio
        r"localhost|"  # localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # IP
        r"(?::\d+)?"  # porta opcional
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    try:
        return bool(pattern.match(url.strip()))
    except Exception:
        return False


def extract_domain(url: str) -> Optional[str]:
    """Extrai o domínio base de uma URL informada."""
    if not is_valid_url(url):
        return None

    # Implementação simplificada via split
    sem_protocolo = url.split("://")[-1]
    dominio_e_resto = sem_protocolo.split("/")[0]
    dominio = dominio_e_resto.split(":")[0]
    return dominio.lower()
