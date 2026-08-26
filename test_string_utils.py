"""
Testes unitários para o módulo StringUtils
"""

import pytest
from string_utils import StringUtils


class TestStringUtils:
    """Testes para a classe StringUtils."""
    
    def setup_method(self):
        """Configuração antes de cada teste."""
        self.s = StringUtils()
    
    # ========== CONVERSÃO ==========
    
    def test_para_maiusculas(self):
        """Testa conversão para maiúsculas."""
        assert self.s.para_maiusculas("hello") == "HELLO"
        assert self.s.para_maiusculas("Hello World") == "HELLO WORLD"
    
    def test_para_minusculas(self):
        """Testa conversão para minúsculas."""
        assert self.s.para_minusculas("HELLO") == "hello"
        assert self.s.para_minusculas("Hello World") == "hello world"
    
    def test_para_titulo(self):
        """Testa conversão para título."""
        assert self.s.para_titulo("hello world") == "Hello World"
        assert self.s.para_titulo("HELLO") == "Hello"
    
    def test_para_camel_case(self):
        """Testa conversão para CamelCase."""
        assert self.s.para_camel_case("meu nome eh joao") == "MeuNomeEhJoao"
        assert self.s.para_camel_case("hello-world") == "HelloWorld"
        assert self.s.para_camel_case("hello_world") == "HelloWorld"
    
    def test_para_snake_case(self):
        """Testa conversão para snake_case."""
        assert self.s.para_snake_case("MeuNomeVariavel") == "meu_nome_variavel"
        assert self.s.para_snake_case("hello world") == "hello_world"
        assert self.s.para_snake_case("hello-world") == "hello_world"
    
    def test_para_kebab_case(self):
        """Testa conversão para kebab-case."""
        assert self.s.para_kebab_case("MeuNomeVariavel") == "meu-nome-variavel"
        assert self.s.para_kebab_case("hello world") == "hello-world"
    
    def test_camel_para_snake(self):
        """Testa conversão CamelCase para snake_case."""
        assert self.s.camel_para_snake("meuNomeVariavel") == "meu_nome_variavel"
        assert self.s.camel_para_snake("HelloWorld") == "hello_world"
    
    def test_snake_para_camel(self):
        """Testa conversão snake_case para CamelCase."""
        assert self.s.snake_para_camel("meu_nome_variavel") == "MeuNomeVariavel"
        assert self.s.snake_para_camel("hello_world") == "HelloWorld"
    
    # ========== LIMPEZA ==========
    
    def test_remover_acentos(self):
        """Testa remoção de acentos."""
        assert self.s.remover_acentos("café") == "cafe"
        assert self.s.remover_acentos("açúcar") == "acucar"
        assert self.s.remover_acentos("coração") == "coracao"
    
    def test_remover_espacos_extras(self):
        """Testa remoção de espaços extras."""
        assert self.s.remover_espacos_extras("  hello   world  ") == "hello world"
        assert self.s.remover_espacos_extras("hello") == "hello"
    
    def test_remover_numeros(self):
        """Testa remoção de números."""
        assert self.s.remover_numeros("teste123") == "teste"
        assert self.s.remover_numeros("123abc456") == "abc"
    
    def test_remover_especiais(self):
        """Testa remoção de caracteres especiais."""
        assert self.s.remover_especiais("hello! @world#") == "hello  world"
        assert self.s.remover_especiais("teste123") == "teste123"
    
    # ========== VALIDAÇÃO ==========
    
    def test_contem_apenas_letras(self):
        """Testa se contém apenas letras."""
        assert self.s.contem_apenas_letras("hello") is True
        assert self.s.contem_apenas_letras("hello123") is False
        assert self.s.contem_apenas_letras("hello world") is False
    
    def test_contem_apenas_numeros(self):
        """Testa se contém apenas números."""
        assert self.s.contem_apenas_numeros("12345") is True
        assert self.s.contem_apenas_numeros("123abc") is False
    
    def test_eh_email(self):
        """Testa validação de email."""
        assert self.s.eh_email("test@email.com") is True
        assert self.s.eh_email("invalid-email") is False
        assert self.s.eh_email("@domain.com") is False
    
    # ========== EXTRAÇÃO ==========
    
    def test_extrair_numeros(self):
        """Testa extração de números."""
        assert self.s.extrair_numeros("teste123abc456") == ["123", "456"]
        assert self.s.extrair_numeros("hello") == []
    
    def test_extrair_emails(self):
        """Testa extração de emails."""
        texto = "Contato: a@b.com ou c@d.org"
        assert self.s.extrair_emails(texto) == ["a@b.com", "c@d.org"]
    
    def test_extrair_urls(self):
        """Testa extração de URLs."""
        texto = "Visite https://google.com ou http://example.com"
        urls = self.s.extrair_urls(texto)
        assert len(urls) == 2
    
    def test_extrair_palavras(self):
        """Testa extração de palavras."""
        assert self.s.extrair_palavras("hello world 123") == ["hello", "world", "123"]
    
    # ========== FORMATAÇÃO ==========
    
    def test_truncar(self):
        """Testa truncamento de texto."""
        assert self.s.truncar("hello world", 5) == "hello..."
        assert self.s.truncar("hello", 10) == "hello"
    
    def test_inverter(self):
        """Testa inversão de texto."""
        assert self.s.inverter("hello") == "olleh"
        assert self.s.inverter("123") == "321"
    
    def test_centralizar(self):
        """Testa centralização de texto."""
        assert self.s.centralizar("hello", 11, "-") == "---hello---"
        assert self.s.centralizar("hello", 10) == "  hello   "
    
    # ========== ANÁLISE ==========
    
    def test_contar_vogais(self):
        """Testa contagem de vogais."""
        assert self.s.contar_vogais("hello") == 2
        assert self.s.contar_vogais("xyz") == 0
    
    def test_contar_consoantes(self):
        """Testa contagem de consoantes."""
        assert self.s.contar_consoantes("hello") == 3
        assert self.s.contar_consoantes("aeiou") == 0
    
    def test_contar_palavras(self):
        """Testa contagem de palavras."""
        assert self.s.contar_palavras("hello world") == 2
        assert self.s.contar_palavras("hello") == 1
    
    def test_frequencia_caracteres(self):
        """Testa frequência de caracteres."""
        freq = self.s.frequencia_caracteres("hello")
        assert freq['h'] == 1
        assert freq['l'] == 2
    
    # ========== BUSCA E SUBSTITUIÇÃO ==========
    
    def test_contem(self):
        """Testa se texto contém substring."""
        assert self.s.contem("hello world", "world") is True
        assert self.s.contem("hello world", "python") is False
    
    def test_substituir(self):
        """Testa substituição de substring."""
        assert self.s.substituir("hello world", "world", "python") == "hello python"
    
    def test_contar_ocorrencias(self):
        """Testa contagem de ocorrências."""
        assert self.s.contar_ocorrencias("hello hello", "hello") == 2
        assert self.s.contar_ocorrencias("hello", "world") == 0


class TestFuncoesAuxiliares:
    """Testes para funções auxiliares."""
    
    def test_para_snake_case(self):
        """Testa função para_snake_case."""
        from string_utils import para_snake_case
        assert para_snake_case("MeuNomeVariavel") == "meu_nome_variavel"
    
    def test_para_camel_case(self):
        """Testa função para_camel_case."""
        from string_utils import para_camel_case
        assert para_camel_case("meu_nome_variavel") == "MeuNomeVariavel"
    
    def test_remover_acentos(self):
        """Testa função remover_acentos."""
        from string_utils import remover_acentos
        assert remover_acentos("café") == "cafe"
    
    def test_truncar(self):
        """Testa função truncar."""
        from string_utils import truncar
        assert truncar("hello world", 5) == "hello..."


if __name__ == "__main__":
    pytest.main([__file__, "-v"])