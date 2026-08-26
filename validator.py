"""
Módulo Validator - Validação de dados

Este módulo fornece funções para validação de diferentes tipos de dados.
"""

import re
from typing import Any, Optional, List, Dict, Tuple


class ValidationError(Exception):
    """Exceção lançada quando uma validação falha."""
    
    def __init__(self, mensagem: str, campo: str = None, valor: Any = None):
        self.mensagem = mensagem
        self.campo = campo
        self.valor = valor
        super().__init__(self.mensagem)


class Validator:
    """
    Classe principal para validação de dados.
    
    Examples:
        >>> validator = Validator()
        >>> validator.validar_email("test@email.com")
        True
        >>> validator.validar_cpf("123.456.789-00")
        True
    """
    
    def __init__(self):
        """Inicializa o Validator."""
        self.erros: List[Dict[str, str]] = []
    
    def limpar_erros(self):
        """Limpa a lista de erros."""
        self.erros = []
    
    def adicionar_erro(self, campo: str, mensagem: str):
        """
        Adiciona um erro à lista.
        
        Args:
            campo: Nome do campo com erro
            mensagem: Descrição do erro
        """
        self.erros.append({"campo": campo, "mensagem": mensagem})
    
    def validar_email(self, email: str) -> bool:
        """
        Valida um endereço de email.
        
        Args:
            email: Email a ser validado
            
        Returns:
            True se válido, False caso contrário
            
        Examples:
            >>> v = Validator()
            >>> v.validar_email("user@example.com")
            True
            >>> v.validar_email("invalid-email")
            False
        """
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        valido = bool(re.match(padrao, email))
        if not valido:
            self.adicionar_erro("email", f"Email inválido: {email}")
        return valido
    
    def validar_cpf(self, cpf: str) -> bool:
        """
        Valida um CPF brasileiro.
        
        Args:
            cpf: CPF a ser validado (com ou sem formatação)
            
        Returns:
            True se válido, False caso contrário
            
        Examples:
            >>> v = Validator()
            >>> v.validar_cpf("123.456.789-09")
            True
        """
        # Remove formatação
        cpf_numeros = re.sub(r'[^0-9]', '', cpf)
        
        # Verifica se tem 11 dígitos
        if len(cpf_numeros) != 11:
            self.adicionar_erro("cpf", "CPF deve ter 11 dígitos")
            return False
        
        # Verifica se todos os dígitos são iguais
        if len(set(cpf_numeros)) == 1:
            self.adicionar_erro("cpf", "CPF com todos dígitos iguais é inválido")
            return False
        
        # Validação dos dígitos verificadores
        def calcular_digito(cpf_parcial: str, peso_inicial: int) -> int:
            soma = sum(int(digito) * peso for digito, peso in 
                      zip(cpf_parcial, range(peso_inicial, 1, -1)))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto
        
        digito1 = calcular_digito(cpf_numeros[:9], 10)
        digito2 = calcular_digito(cpf_numeros[:10], 11)
        
        if cpf_numeros[-2:] != f"{digito1}{digito2}":
            self.adicionar_erro("cpf", "CPF inválido (dígitos verificadores)")
            return False
        
        return True
    
    def validar_cnpj(self, cnpj: str) -> bool:
        """
        Valida um CNPJ brasileiro.
        
        Args:
            cnpj: CNPJ a ser validado (com ou sem formatação)
            
        Returns:
            True se válido, False caso contrário
        """
        # Remove formatação
        cnpj_numeros = re.sub(r'[^0-9]', '', cnpj)
        
        # Verifica se tem 14 dígitos
        if len(cnpj_numeros) != 14:
            self.adicionar_erro("cnpj", "CNPJ deve ter 14 dígitos")
            return False
        
        # Verifica se todos os dígitos são iguais
        if len(set(cnpj_numeros)) == 1:
            self.adicionar_erro("cnpj", "CNPJ com todos dígitos iguais é inválido")
            return False
        
        # Validação dos dígitos verificadores
        def calcular_digito(cnpj_parcial: str, pesos: List[int]) -> int:
            soma = sum(int(digito) * peso for digito, peso in 
                      zip(cnpj_parcial, pesos))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto
        
        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        
        digito1 = calcular_digito(cnpj_numeros[:12], pesos1)
        digito2 = calcular_digito(cnpj_numeros[:13], pesos2)
        
        if cnpj_numeros[-2:] != f"{digito1}{digito2}":
            self.adicionar_erro("cnpj", "CNPJ inválido (dígitos verificadores)")
            return False
        
        return True
    
    def validar_telefone(self, telefone: str) -> bool:
        """
        Valida um número de telefone brasileiro.
        
        Args:
            telefone: Telefone a ser validado
            
        Returns:
            True se válido, False caso contrário
        """
        # Remove formatação
        tel_numeros = re.sub(r'[^0-9]', '', telefone)
        
        # Verifica se tem 10 ou 11 dígitos
        if len(tel_numeros) not in [10, 11]:
            self.adicionar_erro("telefone", "Telefone deve ter 10 ou 11 dígitos")
            return False
        
        # Verifica se começa com DDD válido
        ddd = int(tel_numeros[:2])
        if ddd < 11 or ddd > 99:
            self.adicionar_erro("telefone", "DDD inválido")
            return False
        
        return True
    
    def validar_senha(self, senha: str, min_tamanho: int = 8) -> Tuple[bool, List[str]]:
        """
        Valida a força de uma senha.
        
        Args:
            senha: Senha a ser validada
            min_tamanho: Tamanho mínimo (padrão: 8)
            
        Returns:
            Tupla (válido, lista de requisitos atendidos)
            
        Examples:
            >>> v = Validator()
            >>> valido, requisitos = v.validar_senha("MinhaSenh@123")
            >>> print(valido)
            True
        """
        requisitos = []
        
        # Tamanho mínimo
        if len(senha) >= min_tamanho:
            requisitos.append("tamanho_minimo")
        else:
            self.adicionar_erro("senha", f"Senha deve ter no mínimo {min_tamanho} caracteres")
        
        # Pelo menos uma letra maiúscula
        if re.search(r'[A-Z]', senha):
            requisitos.append("maiuscula")
        else:
            self.adicionar_erro("senha", "Senha deve conter pelo menos uma letra maiúscula")
        
        # Pelo menos uma letra minúscula
        if re.search(r'[a-z]', senha):
            requisitos.append("minuscula")
        else:
            self.adicionar_erro("senha", "Senha deve conter pelo menos uma letra minúscula")
        
        # Pelo menos um número
        if re.search(r'[0-9]', senha):
            requisitos.append("numero")
        else:
            self.adicionar_erro("senha", "Senha deve conter pelo menos um número")
        
        # Pelo menos um caractere especial
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            requisitos.append("especial")
        else:
            self.adicionar_erro("senha", "Senha deve conter pelo menos um caractere especial")
        
        return len(requisitos) == 5, requisitos
    
    def validar_url(self, url: str) -> bool:
        """
        Valida uma URL.
        
        Args:
            url: URL a ser validada
            
        Returns:
            True se válida, False caso contrário
        """
        padrao = r'^https?://[^\s/$.?#].[^\s]*$'
        valido = bool(re.match(padrao, url, re.IGNORECASE))
        if not valido:
            self.adicionar_erro("url", f"URL inválida: {url}")
        return valido
    
    def validar_numero(self, valor: Any, minimo: float = None, maximo: float = None) -> bool:
        """
        Valida se um valor é numérico e está dentro dos limites.
        
        Args:
            valor: Valor a ser validado
            minimo: Valor mínimo (opcional)
            maximo: Valor máximo (opcional)
            
        Returns:
            True se válido, False caso contrário
        """
        try:
            numero = float(valor)
        except (ValueError, TypeError):
            self.adicionar_erro("numero", f"Valor não é numérico: {valor}")
            return False
        
        if minimo is not None and numero < minimo:
            self.adicionar_erro("numero", f"Valor {numero} menor que mínimo {minimo}")
            return False
        
        if maximo is not None and numero > maximo:
            self.adicionar_erro("numero", f"Valor {numero} maior que máximo {maximo}")
            return False
        
        return True
    
    def validar_lista_nao_vazia(self, lista: List[Any], nome_campo: str = "lista") -> bool:
        """
        Valida se uma lista não está vazia.
        
        Args:
            lista: Lista a ser validada
            nome_campo: Nome do campo para mensagem de erro
            
        Returns:
            True se não vazia, False caso contrário
        """
        if not lista or len(lista) == 0:
            self.adicionar_erro(nome_campo, f"{nome_campo} não pode ser vazia")
            return False
        return True
    
    def obter_erros(self) -> List[Dict[str, str]]:
        """
        Retorna a lista de erros acumulados.
        
        Returns:
            Lista de dicionários com campo e mensagem
        """
        return self.erros
    
    def tem_erros(self) -> bool:
        """
        Verifica se há erros acumulados.
        
        Returns:
            True se houver erros
        """
        return len(self.erros) > 0


# Funções auxiliares para uso rápido
def validar_email(email: str) -> bool:
    """Função auxiliar para validar email."""
    return Validator().validar_email(email)


def validar_cpf(cpf: str) -> bool:
    """Função auxiliar para validar CPF."""
    return Validator().validar_cpf(cpf)


def validar_senha(senha: str) -> Tuple[bool, List[str]]:
    """Função auxiliar para validar senha."""
    return Validator().validar_senha(senha)


# Função principal para demonstração
if __name__ == "__main__":
    print("=== Validator - Validação de Dados ===\n")
    
    v = Validator()
    
    # Teste de email
    print("📧 Teste de Email:")
    print(f"  test@email.com: {v.validar_email('test@email.com')}")
    print(f"  invalid-email: {v.validar_email('invalid-email')}")
    
    # Teste de CPF
    print("\n📋 Teste de CPF:")
    print(f"  123.456.789-09: {v.validar_cpf('123.456.789-09')}")
    print(f"  111.111.111-11: {v.validar_cpf('111.111.111-11')}")
    
    # Teste de senha
    print("\n🔒 Teste de Senha:")
    valido, requisitos = v.validar_senha("MinhaSenh@123")
    print(f"  MinhaSenh@123: {valido}")
    print(f"  Requisitos: {requisitos}")
    
    # Teste de URL
    print("\n🌐 Teste de URL:")
    print(f"  https://google.com: {v.validar_url('https://google.com')}")
    print(f"  invalid-url: {v.validar_url('invalid-url')}")
    
    # Resumo de erros
    if v.tem_erros():
        print(f"\n⚠️  Erros encontrados: {len(v.obter_erros())}")
        for erro in v.obter_erros():
            print(f"  - {erro['campo']}: {erro['mensagem']}")