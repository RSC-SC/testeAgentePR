"""Módulo de utilitários para validação, formatação e geração de CPF."""

import random


def extrair_digitos(cpf):
    """Extrai apenas os dígitos numéricos de um CPF."""
    return [int(char) for char in cpf if char.isdigit()]


def validar_cpf(cpf):
    """Retorna True se o CPF for válido segundo o algoritmo de dígitos verificadores."""
    if not cpf:
        return False

    digitos = extrair_digitos(cpf)
    if len(digitos) != 11:
        return False

    # Dígito verificador 1
    soma = sum(d * peso for d, peso in zip(digitos[:9], range(10, 1, -1)))
    resto = soma % 11
    dv1 = 0 if resto < 2 else 11 - resto
    if dv1 != digitos[9]:
        return False

    # Dígito verificador 2
    soma = sum(d * peso for d, peso in zip(digitos[:10], range(11, 1, -1)))
    resto = soma % 11
    dv2 = 0 if resto < 2 else 11 - resto
    if dv2 != digitos[10]:
        return False

    return True


def formatar_cpf(cpf):
    """Formata um CPF no padrão 000.000.000-00."""
    digitos = extrair_digitos(cpf)
    return (
        f"{digitos[0]}{digitos[1]}{digitos[2]}."
        f"{digitos[3]}{digitos[4]}{digitos[5]}."
        f"{digitos[6]}{digitos[7]}{digitos[8]}-"
        f"{digitos[9]}{digitos[10]}"
    )


def mascarar_cpf(cpf):
    """Mascara um CPF mantendo visíveis apenas os 2 últimos dígitos."""
    digitos = extrair_digitos(cpf)
    return f"***.***.***-{digitos[9]}{digitos[10]}"


def gerar_cpf():
    """Gera um CPF válido aleatório (apenas dígitos)."""
    nove = [random.randint(0, 9) for _ in range(9)]

    soma = sum(d * peso for d, peso in zip(nove, range(10, 1, -1)))
    resto = soma % 11
    nove.append(0 if resto < 2 else 11 - resto)

    soma = sum(d * peso for d, peso in zip(nove, range(11, 1, -1)))
    resto = soma % 11
    nove.append(0 if resto < 2 else 11 - resto)

    return "".join(str(d) for d in nove)