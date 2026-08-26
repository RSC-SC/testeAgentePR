"""
Módulo StringUtils - Utilitários para manipulação de strings

Este módulo fornece funções úteis para trabalhar com strings.
"""

import re
import unicodedata
from typing import List, Optional, Tuple


class StringUtils:
    """
    Classe com utilitários para manipulação de strings.
    
    Examples:
        >>> s = StringUtils()
        >>> s.camel_para_snake("meuNomeVariavel")
        'meu_nome_variavel'
        >>> s.inverter("hello")
        'olleh'
    """
    
    def __init__(self):
        """Inicializa o StringUtils."""
        pass
    
    # ========== CONVERSÃO ==========
    
    def para_maiusculas(self, texto: str) -> str:
        """
        Converte texto para maiúsculas.
        
        Args:
            texto: Texto a ser convertido
            
        Returns:
            Texto em maiúsculas
            
        Examples:
            >>> s = StringUtils()
            >>> s.para_maiusculas("hello")
            'HELLO'
        """
        return texto.upper()
    
    def para_minusculas(self, texto: str) -> str:
        """
        Converte texto para minúsculas.
        
        Args:
            texto: Texto a ser convertido
            
        Returns:
            Texto em minúsculas
        """
        return texto.lower()
    
    def para_titulo(self, texto: str) -> str:
        """
        Converte texto para título (primeira letra maiúscula).
        
        Args:
            texto: Texto a ser convertido
            
        Returns:
            Texto em formato título
            
        Examples:
            >>> s = StringUtils()
            >>> s.para_titulo("hello world")
            'Hello World'
        """
        return texto.title()
    
    def para_camel_case(self, texto: str) -> str:
        """
        Converte texto para CamelCase.
        
        Args:
            texto: Texto (pode ter espaços, hífens, underscores)
            
        Returns:
            Texto em CamelCase
            
        Examples:
            >>> s = StringUtils()
            >>> s.para_camel_case("meu nome eh joao")
            'MeuNomeEhJoao'
        """
        # Substitui separadores por espaços
        texto = re.sub(r'[-_]+', ' ', texto)
        # Capitaliza primeira letra de cada palavra
        return ''.join(palavra.capitalize() for palavra in texto.split())
    
    def para_snake_case(self, texto: str) -> str:
        """
        Converte texto para snake_case.
        
        Args:
            texto: Texto (pode ter espaços, CamelCase)
            
        Returns:
            Texto em snake_case
            
        Examples:
            >>> s = StringUtils()
            >>> s.para_snake_case("MeuNomeVariavel")
            'meu_nome_variavel'
        """
        # Insere underscores antes de maiúsculas
        texto = re.sub(r'([A-Z])', r'_\1', texto)
        # Substitui espaços e hífens por underscores
        texto = re.sub(r'[- ]+', '_', texto)
        # Remove underscores duplos e convert para minúsculas
        texto = re.sub(r'_+', '_', texto)
        return texto.lower().strip('_')
    
    def para_kebab_case(self, texto: str) -> str:
        """
        Converte texto para kebab-case.
        
        Args:
            texto: Texto a ser convertido
            
        Returns:
            Texto em kebab-case
            
        Examples:
            >>> s = StringUtils()
            >>> s.para_kebab_case("MeuNomeVariavel")
            'meu-nome-variavel'
        """
        return self.para_snake_case(texto).replace('_', '-')
    
    def camel_para_snake(self, texto: str) -> str:
        """
        Converte CamelCase para snake_case.
        
        Args:
            texto: Texto em CamelCase
            
        Returns:
            Texto em snake_case
            
        Examples:
            >>> s = StringUtils()
            >>> s.camel_para_snake("meuNomeVariavel")
            'meu_nome_variavel'
        """
        texto = re.sub(r'([A-Z])', r'_\1', texto)
        return texto.lower().strip('_')
    
    def snake_para_camel(self, texto: str) -> str:
        """
        Converte snake_case para CamelCase.
        
        Args:
            texto: Texto em snake_case
            
        Returns:
            Texto em CamelCase
            
        Examples:
            >>> s = StringUtils()
            >>> s.snake_para_camel("meu_nome_variavel")
            'MeuNomeVariavel'
        """
        return ''.join(palavra.capitalize() for palavra in texto.split('_'))
    
    # ========== LIMPEZA ==========
    
    def remover_acentos(self, texto: str) -> str:
        """
        Remove acentos de um texto.
        
        Args:
            texto: Texto com acentos
            
        Returns:
            Texto sem acentos
            
        Examples:
            >>> s = StringUtils()
            >>> s.remover_acentos("café")
            'cafe'
        """
        # Normaliza e remove acentos
        texto_normalizado = unicodedata.normalize('NFD', texto)
        return ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    
    def remover_espacos_extras(self, texto: str) -> str:
        """
        Remove espaços extras (múltiplos espaços, espaços no início/fim).
        
        Args:
            texto: Texto com espaços extras
            
        Returns:
            Texto limpo
            
        Examples:
            >>> s = StringUtils()
            >>> s.remover_espacos_extras("  hello   world  ")
            'hello world'
        """
        return ' '.join(texto.split())
    
    def remover_numeros(self, texto: str) -> str:
        """
        Remove todos os números do texto.
        
        Args:
            texto: Texto com números
            
        Returns:
            Texto sem números
            
        Examples:
            >>> s = StringUtils()
            >>> s.remover_numeros("teste123")
            'teste'
        """
        return re.sub(r'\d+', '', texto)
    
    def remover_especiais(self, texto: str) -> str:
        """
        Remove caracteres especiais (mantém apenas alfanuméricos e espaços).
        
        Args:
            texto: Texto com caracteres especiais
            
        Returns:
            Texto limpo
            
        Examples:
            >>> s = StringUtils()
            >>> s.remover_especiais("hello! @world#")
            'hello  world'
        """
        return re.sub(r'[^a-zA-Z0-9\s]', '', texto)
    
    # ========== VALIDAÇÃO ==========
    
    def contem_apenas_letras(self, texto: str) -> bool:
        """
        Verifica se o texto contém apenas letras.
        
        Args:
            texto: Texto a ser verificado
            
        Returns:
            True se contiver apenas letras
            
        Examples:
            >>> s = StringUtils()
            >>> s.contem_apenas_letras("hello")
            True
            >>> s.contem_apenas_letras("hello123")
            False
        """
        return texto.isalpha()
    
    def contem_apenas_numeros(self, texto: str) -> bool:
        """
        Verifica se o texto contém apenas números.
        
        Args:
            texto: Texto a ser verificado
            
        Returns:
            True se contiver apenas números
        """
        return texto.isdigit()
    
    def contem_letras_e_numeros(self, texto: str) -> bool:
        """
        Verifica se o texto contém letras e números.
        
        Args:
            texto: Texto a ser verificado
            
        Returns:
            True se contiver letras e números
        """
        return bool(re.match(r'^[a-zA-Z0-9]+$', texto))
    
    def eh_email(self, texto: str) -> bool:
        """
        Verifica se o texto é um email válido.
        
        Args:
            texto: Texto a ser verificado
            
        Returns:
            True se for um email válido
        """
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao, texto))
    
    # ========== EXTRAÇÃO ==========
    
    def extrair_numeros(self, texto: str) -> List[str]:
        """
        Extrai todos os números do texto.
        
        Args:
            texto: Texto com números
            
        Returns:
            Lista de números encontrados
            
        Examples:
            >>> s = StringUtils()
            >>> s.extrair_numeros("teste123abc456")
            ['123', '456']
        """
        return re.findall(r'\d+', texto)
    
    def extrair_emails(self, texto: str) -> List[str]:
        """
        Extrai todos os emails do texto.
        
        Args:
            texto: Texto com emails
            
        Returns:
            Lista de emails encontrados
            
        Examples:
            >>> s = StringUtils()
            >>> s.extrair_emails("Contato: a@b.com ou c@d.org")
            ['a@b.com', 'c@d.org']
        """
        return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto)
    
    def extrair_urls(self, texto: str) -> List[str]:
        """
        Extrai todas as URLs do texto.
        
        Args:
            texto: Texto com URLs
            
        Returns:
            Lista de URLs encontradas
        """
        padrao = r'https?://[^\s<>\"\'|?^\[\]]+'
        return re.findall(padrao, texto)
    
    def extrair_palavras(self, texto: str) -> List[str]:
        """
        Extrai todas as palavras do texto.
        
        Args:
            texto: Texto com palavras
            
        Returns:
            Lista de palavras
            
        Examples:
            >>> s = StringUtils()
            >>> s.extrair_palavras("hello world 123")
            ['hello', 'world', '123']
        """
        return texto.split()
    
    # ========== FORMATAÇÃO ==========
    
    def truncar(self, texto: str, tamanho: int, sufixo: str = "...") -> str:
        """
        Trunca um texto para o tamanho especificado.
        
        Args:
            texto: Texto a ser truncado
            tamanho: Tamanho máximo
            sufixo: Sufixo a ser adicionado (padrão: "...")
            
        Returns:
            Texto truncado
            
        Examples:
            >>> s = StringUtils()
            >>> s.truncar("hello world", 5)
            'hello...'
        """
        if len(texto) <= tamanho:
            return texto
        return texto[:tamanho] + sufixo
    
    def inverter(self, texto: str) -> str:
        """
        Inverte um texto.
        
        Args:
            texto: Texto a ser invertido
            
        Returns:
            Texto invertido
            
        Examples:
            >>> s = StringUtils()
            >>> s.inverter("hello")
            'olleh'
        """
        return texto[::-1]
    
    def repetir(self, texto: str, vezes: int) -> str:
        """
        Repete um texto várias vezes.
        
        Args:
            texto: Texto a ser repetido
            vezes: Número de vezes
            
        Returns:
            Texto repetido
        """
        return texto * vezes
    
    def centralizar(self, texto: str, largura: int, preenchimento: str = " ") -> str:
        """
        Centraliza um texto com preenchimento.
        
        Args:
            texto: Texto a ser centralizado
            largura: Largura total
            preenchimento: Caractere de preenchimento
            
        Returns:
            Texto centralizado
            
        Examples:
            >>> s = StringUtils()
            >>> s.centralizar("hello", 11, "-")
            '---hello---'
        """
        return texto.center(largura, preenchimento)
    
    # ========== ANÁLISE ==========
    
    def contar_vogais(self, texto: str) -> int:
        """
        Conta o número de vogais no texto.
        
        Args:
            texto: Texto a ser analisado
            
        Returns:
            Número de vogais
            
        Examples:
            >>> s = StringUtils()
            >>> s.contar_vogais("hello")
            2
        """
        return len(re.findall(r'[aeiouAEIOU]', texto))
    
    def contar_consoantes(self, texto: str) -> int:
        """
        Conta o número de consoantes no texto.
        
        Args:
            texto: Texto a ser analisado
            
        Returns:
            Número de consoantes
        """
        return len(re.findall(r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]', texto))
    
    def contar_palavras(self, texto: str) -> int:
        """
        Conta o número de palavras no texto.
        
        Args:
            texto: Texto a ser analisado
            
        Returns:
            Número de palavras
            
        Examples:
            >>> s = StringUtils()
            >>> s.contar_palavras("hello world")
            2
        """
        return len(texto.split())
    
    def contar_caracteres(self, texto: str, incluir_espacos: bool = True) -> int:
        """
        Conta o número de caracteres no texto.
        
        Args:
            texto: Texto a ser analisado
            incluir_espacos: Se deve contar espaços
            
        Returns:
            Número de caracteres
        """
        if incluir_espacos:
            return len(texto)
        return len(texto.replace(" ", ""))
    
    def frequencia_caracteres(self, texto: str) -> dict:
        """
        Calcula a frequência de cada caractere.
        
        Args:
            texto: Texto a ser analisado
            
        Returns:
            Dicionário com frequência de cada caractere
            
        Examples:
            >>> s = StringUtils()
            >>> s.frequencia_caracteres("hello")
            {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        """
        freq = {}
        for char in texto:
            freq[char] = freq.get(char, 0) + 1
        return freq
    
    # ========== BUSCA E SUBSTITUIÇÃO ==========
    
    def contem(self, texto: str, busca: str, case_sensitive: bool = True) -> bool:
        """
        Verifica se o texto contém a substring.
        
        Args:
            texto: Texto a ser buscado
            busca: Substring a ser buscada
            case_sensitive: Se a busca deve ser case sensitive
            
        Returns:
            True se encontrar
        """
        if not case_sensitive:
            texto = texto.lower()
            busca = busca.lower()
        return busca in texto
    
    def substituir(self, texto: str, antigo: str, novo: str) -> str:
        """
        Substitui uma substring por outra.
        
        Args:
            texto: Texto original
            antigo: Substring a ser substituída
            novo: Nova substring
            
        Returns:
            Texto com substituição
            
        Examples:
            >>> s = StringUtils()
            >>> s.substituir("hello world", "world", "python")
            'hello python'
        """
        return texto.replace(antigo, novo)
    
    def contar_ocorrencias(self, texto: str, busca: str) -> int:
        """
        Conta o número de ocorrências de uma substring.
        
        Args:
            texto: Texto a ser buscado
            busca: Substring a ser contada
            
        Returns:
            Número de ocorrências
        """
        return texto.count(busca)


# Funções auxiliares para uso rápido
def para_snake_case(texto: str) -> str:
    """Função auxiliar para converter para snake_case."""
    return StringUtils().para_snake_case(texto)


def para_camel_case(texto: str) -> str:
    """Função auxiliar para converter para CamelCase."""
    return StringUtils().para_camel_case(texto)


def remover_acentos(texto: str) -> str:
    """Função auxiliar para remover acentos."""
    return StringUtils().remover_acentos(texto)


def truncar(texto: str, tamanho: int) -> str:
    """Função auxiliar para truncar texto."""
    return StringUtils().truncar(texto, tamanho)


# Função principal para demonstração
if __name__ == "__main__":
    print("=== StringUtils - Utilitários para Strings ===\n")
    
    s = StringUtils()
    
    # Conversão
    print("🔄 Conversão:")
    print(f"  para_maiusculas: {s.para_maiusculas('hello')}")
    print(f"  para_minusculas: {s.para_minusculas('HELLO')}")
    print(f"  para_titulo: {s.para_titulo('hello world')}")
    print(f"  para_camel_case: {s.para_camel_case('meu nome eh joao')}")
    print(f"  para_snake_case: {s.para_snake_case('MeuNomeVariavel')}")
    print(f"  para_kebab_case: {s.para_kebab_case('MeuNomeVariavel')}")
    print(f"  camel_para_snake: {s.camel_para_snake('meuNomeVariavel')}")
    print(f"  snake_para_camel: {s.snake_para_camel('meu_nome_variavel')}")
    
    # Limpeza
    print("\n🧹 Limpeza:")
    print(f"  remover_acentos: {s.remover_acentos('café')}")
    print(f"  remover_espacos_extras: {s.remover_espacos_extras('  hello   world  ')}")
    print(f"  remover_numeros: {s.remover_numeros('teste123')}")
    print(f"  remover_especiais: {s.remover_especiais('hello! @world#')}")
    
    # Validação
    print("\n✅ Validação:")
    print(f"  contem_apenas_letras: {s.contem_apenas_letras('hello')}")
    print(f"  contem_apenas_numeros: {s.contem_apenas_numeros('123')}")
    print(f"  eh_email: {s.eh_email('test@email.com')}")
    
    # Extração
    print("\n🔍 Extração:")
    print(f"  extrair_numeros: {s.extrair_numeros('teste123abc456')}")
    print(f"  extrair_emails: {s.extrair_emails('a@b.com e c@d.org')}")
    print(f"  extrair_palavras: {s.extrair_palavras('hello world 123')}")
    
    # Formatação
    print("\n📐 Formatação:")
    print(f"  truncar: {s.truncar('hello world', 5)}")
    print(f"  inverter: {s.inverter('hello')}")
    print(f"  centralizar: {s.centralizar('hello', 11, '-')}")
    
    # Análise
    print("\n📊 Análise:")
    print(f"  contar_vogais: {s.contar_vogais('hello')}")
    print(f"  contar_consoantes: {s.contar_consoantes('hello')}")
    print(f"  contar_palavras: {s.contar_palavras('hello world')}")
    print(f"  frequencia_caracteres: {s.frequencia_caracteres('hello')}")
    
    # Busca e Substituição
    print("\n🔎 Busca e Substituição:")
    print(f"  contem: {s.contem('hello world', 'world')}")
    print(f"  substituir: {s.substituir('hello world', 'world', 'python')}")
    print(f"  contar_ocorrencias: {s.contar_ocorrencias('hello hello', 'hello')}")