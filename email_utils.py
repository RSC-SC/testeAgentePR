"""Módulo de utilitários para validação e manipulação de endereços de e-mail."""

import re

_PADRAO_EMAIL = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def validar_email(email):
    """Retorna True se o e-mail for válido segundo o padrão básico."""
    if not email:
        return False
    return bool(_PADRAO_EMAIL.match(email))


def extrair_usuario(email):
    """Retorna a parte local do e-mail (antes do @)."""
    return email.split("@")[0]


def extrair_dominio(email):
    """Retorna o domínio do e-mail em minúsculas."""
    return email.split("@")[1]


def mascarar_email(email):
    """Mascara o e-mail mantendo o primeiro e o último caractere do usuário."""
    usuario = extrair_usuario(email)
    if len(usuario) <= 2:
        mascara = usuario[0] + "**"
    else:
        mascara = usuario[0] + "*" * (len(usuario) - 2) + usuario[-1]
    return f"{mascara}@{extrair_dominio(email)}"


def normalizar_email(email):
    """Normaliza o e-mail: remove espaços e converte para minúsculas."""
    if not email:
        return ""
    return email.strip().lower()


def eh_email_institucional(email, dominios):
    """Retorna True se o domínio do e-mail estiver na lista de domínios permitidos."""
    dominio = extrair_dominio(email)
    return dominio in dominios