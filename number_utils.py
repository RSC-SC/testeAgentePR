"""Módulo de utilitários para operações numéricas e formatação de números."""

import math


def arredondar(valor, casas=2):
    """Arredonda um valor para o número de casas decimais informado."""
    return round(valor, casas)


def formatar_moeda(valor, simbolo="R$"):
    """Formata um valor numérico como moeda no padrão brasileiro (ex.: R$ 1.234,56)."""
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = (
        valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    )
    return f"{simbolo} {valor_formatado}"


def porcentagem(parte, total):
    """Calcula o percentual que 'parte' representa de 'total'."""
    return round((parte * 100) / total, 2)


def eh_par(numero):
    """Retorna True se o número informado for par."""
    return numero % 2 == 0


def eh_primo(numero):
    """Retorna True se o número informado for primo."""
    if numero < 2:
        return False
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True


def fatorial(numero):
    """Calcula o fatorial de um número inteiro não negativo."""
    if numero == 0:
        return 1
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


def somar(numeros):
    """Soma todos os números de uma lista ou tupla."""
    total = 0
    for numero in numeros:
        total += numero
    return total


def raiz_quadrada(numero):
    """Calcula a raiz quadrada de um número não negativo."""
    return math.sqrt(numero)


def media(numeros):
    """Calcula a média aritmética de uma lista de números."""
    return somar(numeros) / len(numeros)