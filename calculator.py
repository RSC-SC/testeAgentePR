"""
Módulo Calculator - Funções básicas de cálculo

Este módulo fornece implementações de operações matemáticas básicas.
"""


def somar(a: float, b: float) -> float:
    """
    Retorna a soma de dois números.
    
    Args:
        a: Primeiro número
        b: Segundo número
        
    Returns:
        Resultado da soma
        
    Examples:
        >>> somar(2, 3)
        5
        >>> somar(-1, 1)
        0
    """
    return a + b


def subtrair(a: float, b: float) -> float:
    """
    Retorna a subtração de dois números.
    
    Args:
        a: Primeiro número
        b: Segundo número
        
    Returns:
        Resultado da subtração
        
    Examples:
        >>> subtrair(10, 4)
        6
        >>> subtrair(5, 5)
        0
    """
    return a - b


def multiplicar(a: float, b: float) -> float:
    """
    Retorna a multiplicação de dois números.
    
    Args:
        a: Primeiro número
        b: Segundo número
        
    Returns:
        Resultado da multiplicação
        
    Examples:
        >>> multiplicar(5, 5)
        25
        >>> multiplicar(3, 0)
        0
    """
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Retorna a divisão de dois números.
    
    Args:
        a: Dividendo
        b: Divisor
        
    Returns:
        Resultado da divisão
        
    Raises:
        ValueError: Se o divisor for zero
        
    Examples:
        >>> dividir(10, 2)
        5.0
        >>> dividir(7, 2)
        3.5
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


def potencia(base: float, expoente: float) -> float:
    """
    Retorna a potenciação de um número.
    
    Args:
        base: Base da potenciação
        expoente: Expoente
        
    Returns:
        Resultado da potenciação
        
    Examples:
        >>> potencia(2, 3)
        8
        >>> potencia(5, 2)
        25
    """
    return base ** expoente


def raiz_quadrada(numero: float) -> float:
    """
    Retorna a raiz quadrada de um número.
    
    Args:
        numero: Número positivo
        
    Returns:
        Raiz quadrada do número
        
    Raises:
        ValueError: Se o número for negativo
        
    Examples:
        >>> raiz_quadrada(9)
        3.0
        >>> raiz_quadrada(16)
        4.0
    """
    if numero < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo")
    return numero ** 0.5


# Função principal para demonstração
if __name__ == "__main__":
    print("=== Calculadora Simples ===")
    print(f"2 + 3 = {somar(2, 3)}")
    print(f"10 - 4 = {subtrair(10, 4)}")
    print(f"5 * 5 = {multiplicar(5, 5)}")
    print(f"10 / 2 = {dividir(10, 2)}")
    print(f"2 ^ 3 = {potencia(2, 3)}")
    print(f"√9 = {raiz_quadrada(9)}")