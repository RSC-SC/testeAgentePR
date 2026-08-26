"""
Testes unitários para o módulo FakeData
"""

import pytest
import re
from datetime import datetime
from fake_data import FakeData


class TestFakeData:
    """Testes para a classe FakeData."""
    
    def setup_method(self):
        """Configuração antes de cada teste."""
        self.fake = FakeData(seed=42)
    
    # ========== NOMES ==========
    
    def test_nome(self):
        """Testa geração de nome."""
        nome = self.fake.nome()
        assert isinstance(nome, str)
        assert len(nome.split()) >= 2  # Pelo menos primeiro e sobrenome
    
    def test_nome_masculino(self):
        """Testa geração de nome masculino."""
        nome = self.fake.nome(masculino=True)
        assert isinstance(nome, str)
    
    def test_nome_feminino(self):
        """Testa geração de nome feminino."""
        nome = self.fake.nome(masculino=False)
        assert isinstance(nome, str)
    
    def test_primeiro_nome(self):
        """Testa geração de primeiro nome."""
        primeiro = self.fake.primeiro_nome()
        assert isinstance(primeiro, str)
        assert len(primeiro.split()) == 1
    
    def test_sobrenome(self):
        """Testa geração de sobrenome."""
        sobrenome = self.fake.sobrenome()
        assert isinstance(sobrenome, str)
    
    # ========== DOCUMENTOS ==========
    
    def test_cpf_formatado(self):
        """Testa geração de CPF formatado."""
        cpf = self.fake.cpf(formatado=True)
        # Formato: XXX.XXX.XXX-XX
        assert re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf)
    
    def test_cpf_numeros(self):
        """Testa geração de CPF apenas números."""
        cpf = self.fake.cpf(formatado=False)
        assert re.match(r'^\d{11}$', cpf)
    
    def test_cpf_valido(self):
        """Testa se o CPF gerado é válido."""
        cpf = self.fake.cpf(formatado=False)
        
        # Validação básica de CPF
        if len(set(cpf)) == 1:
            pytest.skip("CPF com todos dígitos iguais (geração aleatória)")
        
        # Validação dos dígitos verificadores
        def calcular_digito(numeros, peso):
            soma = sum(int(n) * p for n, p in zip(numeros, range(peso, 1, -1)))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto
        
        digito1 = calcular_digito(cpf[:9], 10)
        digito2 = calcular_digito(cpf[:10], 11)
        
        assert cpf[-2:] == f"{digito1}{digito2}"
    
    def test_cnpj_formatado(self):
        """Testa geração de CNPJ formatado."""
        cnpj = self.fake.cnpj(formatado=True)
        # Formato: XX.XXX.XXX/XXXX-XX
        assert re.match(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', cnpj)
    
    def test_cnpj_numeros(self):
        """Testa geração de CNPJ apenas números."""
        cnpj = self.fake.cnpj(formatado=False)
        assert re.match(r'^\d{14}$', cnpj)
    
    # ========== CONTATO ==========
    
    def test_email(self):
        """Testa geração de email."""
        email = self.fake.email()
        assert '@' in email
        assert '.' in email.split('@')[1]
    
    def test_email_com_nome(self):
        """Testa geração de email com nome específico."""
        email = self.fake.email("João Silva")
        assert 'joao.silva' in email.lower()
    
    def test_telefone_formatado(self):
        """Testa geração de telefone formatado."""
        telefone = self.fake.telefone(formatado=True)
        # Formato: (XX) XXXXX-XXXX ou (XXXX) XXXX-XXXX
        assert re.match(r'^\(\d{2}\)\s\d{4,5}-\d{4}$', telefone)
    
    def test_celular_formatado(self):
        """Testa geração de celular formatado."""
        celular = self.fake.celular(formatado=True)
        # Formato: (XX) 9XXXX-XXXX
        assert re.match(r'^\(\d{2}\)\s9\d{4}-\d{4}$', celular)
    
    # ========== ENDEREÇO ==========
    
    def test_endereco(self):
        """Testa geração de endereço."""
        endereco = self.fake.endereco()
        assert isinstance(endereco, str)
        assert len(endereco) > 20
    
    def test_cep(self):
        """Testa geração de CEP."""
        cep = self.fake.cep()
        assert re.match(r'^\d{5}-\d{3}$', cep)
    
    def test_cidade(self):
        """Testa geração de cidade."""
        cidade = self.fake.cidade()
        assert isinstance(cidade, str)
        assert len(cidade) > 2
    
    def test_estado(self):
        """Testa geração de estado."""
        estado = self.fake.estado()
        assert len(estado) == 2
        assert estado.isalpha()
    
    # ========== DATA E HORA ==========
    
    def test_data(self):
        """Testa geração de data."""
        data = self.fake.data()
        assert isinstance(data, datetime)
        assert data.year >= 2020
        assert data.year <= datetime.now().year
    
    def test_data_formatada(self):
        """Testa geração de data formatada."""
        data = self.fake.data_formatada()
        assert re.match(r'^\d{2}/\d{2}/\d{4}$', data)
    
    def test_hora(self):
        """Testa geração de hora."""
        hora = self.fake.hora()
        assert re.match(r'^\d{2}:\d{2}$', hora)
    
    def test_data_hora(self):
        """Testa geração de data e hora."""
        data_hora = self.fake.data_hora()
        assert isinstance(data_hora, datetime)
    
    # ========== NÚMEROS E TEXTO ==========
    
    def test_numero(self):
        """Testa geração de número."""
        num = self.fake.numero(1, 100)
        assert isinstance(num, int)
        assert 1 <= num <= 100
    
    def test_decimal(self):
        """Testa geração de decimal."""
        dec = self.fake.decimal(0, 100, 2)
        assert isinstance(dec, float)
        assert 0 <= dec <= 100
    
    def test_texto(self):
        """Testa geração de texto."""
        texto = self.fake.texto(50)
        assert isinstance(texto, str)
        assert len(texto) <= 50
    
    def test_palavra(self):
        """Testa geração de palavra."""
        palavra = self.fake.palavra(8)
        assert isinstance(palavra, str)
        assert len(palavra) == 8
        assert palavra.isalpha()
    
    def test_frase(self):
        """Testa geração de frase."""
        frase = self.fake.frase(8)
        assert isinstance(frase, str)
        assert len(frase.split()) == 8
    
    # ========== EMPRESA ==========
    
    def test_empresa(self):
        """Testa geração de empresa."""
        empresa = self.fake.empresa()
        assert isinstance(empresa, str)
    
    def test_cnae(self):
        """Testa geração de CNAE."""
        cnae = self.fake.cnae()
        assert re.match(r'^\d{2}\.\d{2}-\d$', cnae)
    
    def test_produto(self):
        """Testa geração de produto."""
        produto = self.fake.produto()
        assert isinstance(produto, str)
    
    def test_preco(self):
        """Testa geração de preço."""
        preco = self.fake.preco()
        assert 'R$' in preco
    
    # ========== CARTÃO ==========
    
    def test_numero_cartao(self):
        """Testa geração de número de cartão."""
        cartao = self.fake.numero_cartao()
        assert re.match(r'^\d{4} \d{4} \d{4} \d{4}$', cartao)
    
    def test_validade_cartao(self):
        """Testa geração de validade."""
        validade = self.fake.validade_cartao()
        assert re.match(r'^\d{2}/\d{2}$', validade)
    
    def test_cvv(self):
        """Testa geração de CVV."""
        cvv = self.fake.cvv()
        assert re.match(r'^\d{3}$', cvv)
    
    # ========== LISTAS ==========
    
    def test_lista_nomes(self):
        """Testa geração de lista de nomes."""
        nomes = self.fake.lista_nomes(5)
        assert len(nomes) == 5
        assert all(isinstance(n, str) for n in nomes)
    
    def test_lista_emails(self):
        """Testa geração de lista de emails."""
        emails = self.fake.lista_emails(5)
        assert len(emails) == 5
        assert all('@' in e for e in emails)
    
    def test_lista_cpfs(self):
        """Testa geração de lista de CPFs."""
        cpfs = self.fake.lista_cpfs(5)
        assert len(cpfs) == 5
    
    # ========== DICIONÁRIOS ==========
    
    def test_pessoa(self):
        """Testa geração de pessoa completa."""
        pessoa = self.fake.pessoa()
        assert 'nome' in pessoa
        assert 'cpf' in pessoa
        assert 'email' in pessoa
        assert 'telefone' in pessoa
        assert 'endereco' in pessoa
    
    def test_empresa_completa(self):
        """Testa geração de empresa completa."""
        empresa = self.fake.empresa_completa()
        assert 'razao_social' in empresa
        assert 'cnpj' in empresa
        assert 'email' in empresa


class TestReprodutibilidade:
    """Testes para verificar reprodutibilidade com seed."""
    
    def test_mesma_seed_mesmo_resultado(self):
        """Testa se mesma seed gera mesmo resultado."""
        fake1 = FakeData(seed=123)
        fake2 = FakeData(seed=123)
        
        assert fake1.nome() == fake2.nome()
        assert fake1.cpf() == fake2.cpf()
        assert fake1.email() == fake2.email()
    
    def test_seeds_diferentes_resultados_diferentes(self):
        """Testa se seeds diferentes geram resultados diferentes."""
        fake1 = FakeData(seed=123)
        fake2 = FakeData(seed=456)
        
        # Com seed diferente, pelo menos um valor deve ser diferente
        # (não garantido, mas muito provável)
        assert fake1.palavra() != fake2.palavra() or fake1.numero() != fake2.numero()


class TestFuncoesAuxiliares:
    """Testes para funções auxiliares."""
    
    def test_nome(self):
        """Testa função nome."""
        from fake_data import nome
        assert isinstance(nome(), str)
    
    def test_cpf(self):
        """Testa função cpf."""
        from fake_data import cpf
        assert len(cpf()) == 14  # XXX.XXX.XXX-XX
    
    def test_email(self):
        """Testa função email."""
        from fake_data import email
        assert '@' in email()
    
    def test_telefone(self):
        """Testa função telefone."""
        from fake_data import telefone
        assert '(' in telefone()
    
    def test_endereco(self):
        """Testa função endereco."""
        from fake_data import endereco
        assert isinstance(endereco(), str)
    
    def test_data(self):
        """Testa função data."""
        from fake_data import data
        assert re.match(r'^\d{2}/\d{2}/\d{4}$', data())


if __name__ == "__main__":
    pytest.main([__file__, "-v"])