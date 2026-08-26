"""
Módulo FakeData - Geração de dados falsos

Este módulo fornece funções para gerar dados falsos realistas para testes.
"""

import random
import string
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any


class FakeData:
    """
    Classe para geração de dados falsos.
    
    Supports:
        - Nomes brasileiros
        - CPFs e CNPJs válidos
        - Emails, telefones, endereços
        - Datas, números, textos
        - Dados de empresa, cartão de crédito
    
    Examples:
        >>> fake = FakeData()
        >>> fake.nome()
        'Maria Silva Santos'
        >>> fake.cpf()
        '123.456.789-09'
        >>> fake.email()
        'maria.santos@email.com'
    """
    
    # Listas de dados para geração
    PRIMEIROS_NOMES_M = [
        "João", "Pedro", "Lucas", "Mateus", "Gabriel", "Rafael", "Carlos",
        "Marcos", "André", "Antônio", "Francisco", "Paulo", "Felipe",
        "Alexandre", "Bruno", "Daniel", "Eduardo", "Fernando", "Gustavo"
    ]
    
    PRIMEIROS_NOMES_F = [
        "Maria", "Ana", "Juliana", "Fernanda", "Patricia", "Camila",
        "Amanda", "Bruna", "Letícia", "Gabriela", "Larissa", "Mariana",
        "Carla", "Daniela", "Beatriz", "Vanessa", "Renata", "Adriana"
    ]
    
    SOBRENOMES = [
        "Silva", "Santos", "Souza", "Oliveira", "Ferreira", "Pereira",
        "Almeida", "Ribeiro", "Costa", "Rodrigues", "Nascimento", "Lima",
        "Araújo", "Barbosa", "Gomes", "Martins", "Rocha", "Ramos"
    ]
    
    DOMINIOS_EMAIL = [
        "gmail.com", "hotmail.com", "outlook.com", "yahoo.com",
        "uol.com.br", "bol.com.br", "ig.com.br", "terra.com.br"
    ]
    
    LOGRADOUROS = [
        "Rua", "Avenida", "Travessa", "Alameda", "Praça", "Estrada"
    ]
    
    NOMES_RUA = [
        "das Flores", "do Comércio", "São Paulo", "Brasil", "Liberdade",
        "Tiradentes", "Getúlio Vargas", "Juscelino Kubitschek", "Paulista"
    ]
    
    BAIRROS = [
        "Centro", "Jardim América", "Vila Nova", "Bela Vista",
        "Santa Cruz", "São José", "Parque Industrial"
    ]
    
    CIDADES = [
        "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador",
        "Brasília", "Fortaleza", "Curitiba", "Manaus", "Recife", "Porto Alegre"
    ]
    
    ESTADOS = [
        "SP", "RJ", "MG", "BA", "DF", "CE", "PR", "AM", "PE", "RS"
    ]
    
    EMPRESAS = [
        "Tech Solutions", "Digital Systems", "Innovation Corp", "Data Tech",
        "Smart Solutions", "Future Systems", "Cloud Tech", "AI Solutions"
    ]
    
    PRODUTOS = [
        "Notebook", "Smartphone", "Tablet", "Monitor", "Teclado",
        "Mouse", "Headfone", "Webcam", "Impressora", "HD Externo"
    ]
    
    def __init__(self, seed: Optional[int] = None):
        """
        Inicializa o FakeData.
        
        Args:
            seed: Semente para geração reproduzível (opcional)
        """
        if seed is not None:
            random.seed(seed)
    
    # ========== NOMES ==========
    
    def nome(self, masculino: Optional[bool] = None) -> str:
        """
        Gera um nome brasileiro.
        
        Args:
            masculino: True para masculino, False para feminino, None para aleatório
            
        Returns:
            Nome completo
            
        Examples:
            >>> fake = FakeData()
            >>> fake.nome()
            'Maria Silva Santos'
        """
        if masculino is None:
            masculino = random.choice([True, False])
        
        if masculino:
            primeiro = random.choice(self.PRIMEIROS_NOMES_M)
        else:
            primeiro = random.choice(self.PRIMEIROS_NOMES_F)
        
        sobrenome1 = random.choice(self.SOBRENOMES)
        sobrenome2 = random.choice(self.SOBRENOMES)
        
        return f"{primeiro} {sobrenome1} {sobrenome2}"
    
    def primeiro_nome(self, masculino: Optional[bool] = None) -> str:
        """
        Gera apenas o primeiro nome.
        
        Args:
            masculino: True para masculino, False para feminino
            
        Returns:
            Primeiro nome
        """
        if masculino is None:
            masculino = random.choice([True, False])
        
        if masculino:
            return random.choice(self.PRIMEIROS_NOMES_M)
        return random.choice(self.PRIMEIROS_NOMES_F)
    
    def sobrenome(self) -> str:
        """
        Gera um sobrenome.
        
        Returns:
            Sobrenome
        """
        return random.choice(self.SOBRENOMES)
    
    # ========== DOCUMENTOS ==========
    
    def _calcular_digito_cpf(self, numeros: str, peso: int) -> int:
        """Calcula dígito verificador do CPF."""
        soma = sum(int(n) * p for n, p in zip(numeros, range(peso, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    def cpf(self, formatado: bool = True) -> str:
        """
        Gera um CPF válido.
        
        Args:
            formatado: Se deve retornar formatado (XXX.XXX.XXX-XX)
            
        Returns:
            CPF válido
            
        Examples:
            >>> fake = FakeData()
            >>> fake.cpf()
            '123.456.789-09'
        """
        # Gera 9 números aleatórios
        numeros = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        
        # Calcula dígitos verificadores
        digito1 = self._calcular_digito_cpf(numeros, 10)
        digito2 = self._calcular_digito_cpf(numeros + str(digito1), 11)
        
        cpf_numeros = numeros + f"{digito1}{digito2}"
        
        if formatado:
            return f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
        return cpf_numeros
    
    def _calcular_digito_cnpj(self, numeros: str, pesos: List[int]) -> int:
        """Calcula dígito verificador do CNPJ."""
        soma = sum(int(n) * p for n, p in zip(numeros, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    def cnpj(self, formatado: bool = True) -> str:
        """
        Gera um CNPJ válido.
        
        Args:
            formatado: Se deve retornar formatado (XX.XXX.XXX/XXXX-XX)
            
        Returns:
            CNPJ válido
        """
        # Gera 12 números aleatórios
        numeros = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        
        # Calcula dígitos verificadores
        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        
        digito1 = self._calcular_digito_cnpj(numeros, pesos1)
        digito2 = self._calcular_digito_cnpj(numeros + str(digito1), pesos2)
        
        cnpj_numeros = numeros + f"{digito1}{digito2}"
        
        if formatado:
            return f"{cnpj_numeros[:2]}.{cnpj_numeros[2:5]}.{cnpj_numeros[5:8]}/{cnpj_numeros[8:12]}-{cnpj_numeros[12:]}"
        return cnpj_numeros
    
    # ========== CONTATO ==========
    
    def email(self, nome: Optional[str] = None) -> str:
        """
        Gera um email.
        
        Args:
            nome: Nome para usar no email (opcional)
            
        Returns:
            Email
            
        Examples:
            >>> fake = FakeData()
            >>> fake.email()
            'maria.santos@gmail.com'
        """
        if nome:
            # Limpa o nome
            email_nome = nome.lower().replace(' ', '.')
            email_nome = ''.join(c for c in email_nome if c.isalnum() or c == '.')
        else:
            email_nome = f"{self.primeiro_nome().lower()}.{self.sobrenome().lower()}"
        
        dominio = random.choice(self.DOMINIOS_EMAIL)
        return f"{email_nome}@{dominio}"
    
    def telefone(self, formatado: bool = True) -> str:
        """
        Gera um telefone brasileiro.
        
        Args:
            formatado: Se deve retornar formatado
            
        Returns:
            Telefone
        """
        ddd = random.randint(11, 99)
        
        # Celular começa com 9, fixo com 2-5
        if random.choice([True, False]):  # Celular
            numero = f"9{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
        else:  # Fixo
            numero = f"{random.randint(2, 5)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
        
        if formatado:
            if len(numero) == 9:  # Celular
                return f"({ddd}) {numero[:5]}-{numero[5:]}"
            else:  # Fixo
                return f"({ddd}) {numero[:4]}-{numero[4:]}"
        
        return f"{ddd}{numero}"
    
    def celular(self, formatado: bool = True) -> str:
        """
        Gera um celular brasileiro.
        
        Args:
            formatado: Se deve retornar formatado
            
        Returns:
            Celular
        """
        ddd = random.randint(11, 99)
        numero = f"9{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
        
        if formatado:
            return f"({ddd}) {numero[:5]}-{numero[5:]}"
        return f"{ddd}{numero}"
    
    # ========== ENDEREÇO ==========
    
    def logradouro(self) -> str:
        """
        Gera um logradouro.
        
        Returns:
            Logradouro
        """
        return random.choice(self.LOGRADOUROS)
    
    def rua(self) -> str:
        """
        Gera uma rua.
        
        Returns:
            Nome da rua
        """
        return random.choice(self.NOMES_RUA)
    
    def endereco(self, formatado: bool = True) -> str:
        """
        Gera um endereço completo.
        
        Args:
            formatado: Se deve retornar formatado
            
        Returns:
            Endereço
        """
        logradouro = self.logradouro()
        rua = self.rua()
        numero = random.randint(1, 9999)
        bairro = random.choice(self.BAIRROS)
        cidade = random.choice(self.CIDADES)
        estado = random.choice(self.ESTADOS)
        cep = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"
        
        if formatado:
            return f"{logradouro} {rua}, {numero} - {bairro}, {cidade} - {estado}, {cep}"
        
        return f"{logradouro} {rua} {numero} {bairro} {cidade} {estado} {cep}"
    
    def cep(self) -> str:
        """
        Gera um CEP.
        
        Returns:
            CEP no formato XXXXX-XXX
        """
        return f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"
    
    def cidade(self) -> str:
        """
        Gera uma cidade.
        
        Returns:
            Nome da cidade
        """
        return random.choice(self.CIDADES)
    
    def estado(self) -> str:
        """
        Gera uma sigla de estado.
        
        Returns:
            Sigla do estado
        """
        return random.choice(self.ESTADOS)
    
    # ========== DATA E HORA ==========
    
    def data(self, inicio: Optional[datetime] = None, fim: Optional[datetime] = None) -> datetime:
        """
        Gera uma data aleatória.
        
        Args:
            inicio: Data mínima (padrão: 01/01/2020)
            fim: Data máxima (padrão: hoje)
            
        Returns:
            Data aleatória
        """
        if inicio is None:
            inicio = datetime(2020, 1, 1)
        if fim is None:
            fim = datetime.now()
        
        delta = (fim - inicio).days
        dias_aleatorios = random.randint(0, delta)
        return inicio + timedelta(days=dias_aleatorios)
    
    def data_formatada(self, formato: str = "%d/%m/%Y") -> str:
        """
        Gera uma data formatada.
        
        Args:
            formato: Formato da data
            
        Returns:
            Data formatada
        """
        return self.data().strftime(formato)
    
    def hora(self) -> str:
        """
        Gera uma hora aleatória.
        
        Returns:
            Hora no formato HH:MM
        """
        hora = random.randint(0, 23)
        minuto = random.randint(0, 59)
        return f"{hora:02d}:{minuto:02d}"
    
    def data_hora(self) -> datetime:
        """
        Gera data e hora aleatórias.
        
        Returns:
            Data e hora
        """
        data = self.data()
        hora = random.randint(0, 23)
        minuto = random.randint(0, 59)
        segundo = random.randint(0, 59)
        return data.replace(hour=hora, minute=minuto, second=segundo)
    
    # ========== NÚMEROS E TEXTO ==========
    
    def numero(self, minimo: int = 0, maximo: int = 1000) -> int:
        """
        Gera um número inteiro aleatório.
        
        Args:
            minimo: Valor mínimo
            maximo: Valor máximo
            
        Returns:
            Número inteiro
        """
        return random.randint(minimo, maximo)
    
    def decimal(self, minimo: float = 0, maximo: float = 1000, casas: int = 2) -> float:
        """
        Gera um número decimal aleatório.
        
        Args:
            minimo: Valor mínimo
            maximo: Valor máximo
            casas: Casas decimais
            
        Returns:
            Número decimal
        """
        return round(random.uniform(minimo, maximo), casas)
    
    def texto(self, tamanho: int = 100) -> str:
        """
        Gera texto aleatório.
        
        Args:
            tamanho: Tamanho do texto
            
        Returns:
            Texto aleatório
        """
        palavras = [
            "lorem", "ipsum", "dolor", "sit", "amet", "consectetur",
            "adipiscing", "elit", "sed", "do", "eiusmod", "tempor"
        ]
        return ' '.join(random.choices(palavras, k=tamanho // 6))[:tamanho]
    
    def palavra(self, tamanho: int = 8) -> str:
        """
        Gera uma palavra aleatória.
        
        Args:
            tamanho: Tamanho da palavra
            
        Returns:
            Palavra aleatória
        """
        return ''.join(random.choices(string.ascii_lowercase, k=tamanho))
    
    def frase(self, num_palavras: int = 10) -> str:
        """
        Gera uma frase aleatória.
        
        Args:
            num_palavras: Número de palavras
            
        Returns:
            Frase aleatória
        """
        palavras = [
            "O", "projeto", "está", "avançando", "bem", "e",
            "esperamos", "entregar", "resultados", "excelentes",
            "para", "os", "clientes", "da", "empresa"
        ]
        return ' '.join(random.choices(palavras, k=num_palavras))
    
    # ========== DADOS DE EMPRESA ==========
    
    def empresa(self) -> str:
        """
        Gera um nome de empresa.
        
        Returns:
            Nome da empresa
        """
        return f"{random.choice(['Tech', 'Digital', 'Smart', 'Cloud'])} {random.choice(['Solutions', 'Systems', 'Corp', 'Inc'])}"
    
    def cnae(self) -> str:
        """
        Gera um código CNAE.
        
        Returns:
            Código CNAE
        """
        return f"{random.randint(10, 99)}.{random.randint(10, 99)}-{random.randint(1, 9)}"
    
    def produto(self) -> str:
        """
        Gera um nome de produto.
        
        Returns:
            Nome do produto
        """
        return random.choice(self.PRODUTOS)
    
    def preco(self, minimo: float = 10, maximo: float = 5000) -> str:
        """
        Gera um preço formatado.
        
        Args:
            minimo: Preço mínimo
            maximo: Preço máximo
            
        Returns:
            Preço formatado em R$
        """
        valor = self.decimal(minimo, maximo, 2)
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    # ========== DADOS DE CARTÃO ==========
    
    def numero_cartao(self) -> str:
        """
        Gera um número de cartão de crédito válido (Luhn).
        
        Returns:
            Número do cartão
        """
        # Gera 15 números
        numeros = [random.randint(0, 9) for _ in range(15)]
        
        # Calcula dígito verificador (Luhn)
        soma = 0
        for i, n in enumerate(reversed(numeros)):
            if i % 2 == 0:
                n *= 2
                if n > 9:
                    n -= 9
            soma += n
        
        digito = (10 - (soma % 10)) % 10
        numeros.append(digito)
        
        # Formata
        cartao = ''.join(map(str, numeros))
        return f"{cartao[:4]} {cartao[4:8]} {cartao[8:12]} {cartao[12:]}"
    
    def validade_cartao(self) -> str:
        """
        Gera uma data de validade de cartão.
        
        Returns:
            Validade no formato MM/AA
        """
        mes = random.randint(1, 12)
        ano = random.randint(25, 30)
        return f"{mes:02d}/{ano}"
    
    def cvv(self) -> str:
        """
        Gera um CVV.
        
        Returns:
            CVV de 3 dígitos
        """
        return f"{random.randint(100, 999)}"
    
    # ========== LISTAS ==========
    
    def lista_nomes(self, quantidade: int = 5) -> List[str]:
        """
        Gera uma lista de nomes.
        
        Args:
            quantidade: Número de nomes
            
        Returns:
            Lista de nomes
        """
        return [self.nome() for _ in range(quantidade)]
    
    def lista_emails(self, quantidade: int = 5) -> List[str]:
        """
        Gera uma lista de emails.
        
        Args:
            quantidade: Número de emails
            
        Returns:
            Lista de emails
        """
        return [self.email() for _ in range(quantidade)]
    
    def lista_cpfs(self, quantidade: int = 5) -> List[str]:
        """
        Gera uma lista de CPFs.
        
        Args:
            quantidade: Número de CPFs
            
        Returns:
            Lista de CPFs
        """
        return [self.cpf() for _ in range(quantidade)]
    
    def lista_telefones(self, quantidade: int = 5) -> List[str]:
        """
        Gera uma lista de telefones.
        
        Args:
            quantidade: Número de telefones
            
        Returns:
            Lista de telefones
        """
        return [self.telefone() for _ in range(quantidade)]
    
    def lista_enderecos(self, quantidade: int = 5) -> List[str]:
        """
        Gera uma lista de endereços.
        
        Args:
            quantidade: Número de endereços
            
        Returns:
            Lista de endereços
        """
        return [self.endereco() for _ in range(quantidade)]
    
    # ========== DICIONÁRIO COMPLETO ==========
    
    def pessoa(self) -> Dict[str, Any]:
        """
        Gera um dicionário com dados completos de uma pessoa.
        
        Returns:
            Dicionário com todos os dados
            
        Examples:
            >>> fake = FakeData()
            >>> fake.pessoa()
            {
                'nome': 'Maria Silva Santos',
                'cpf': '123.456.789-09',
                'email': 'maria.santos@gmail.com',
                'telefone': '(11) 99999-9999',
                'endereco': 'Rua das Flores, 123 - Centro, São Paulo - SP, 01234-567',
                'data_nascimento': '15/03/1990'
            }
        """
        nome = self.nome()
        return {
            "nome": nome,
            "cpf": self.cpf(),
            "email": self.email(nome),
            "telefone": self.telefone(),
            "celular": self.celular(),
            "endereco": self.endereco(),
            "cep": self.cep(),
            "cidade": self.cidade(),
            "estado": self.estado(),
            "data_nascimento": self.data_formatada()
        }
    
    def empresa_completa(self) -> Dict[str, Any]:
        """
        Gera um dicionário com dados completos de uma empresa.
        
        Returns:
            Dicionário com dados da empresa
        """
        return {
            "razao_social": self.empresa(),
            "cnpj": self.cnpj(),
            "email": self.email("contato"),
            "telefone": self.telefone(),
            "endereco": self.endereco(),
            "cnae": self.cnae(),
            "funcionarios": self.numero(10, 1000)
        }


# Funções auxiliares para uso rápido
def nome() -> str:
    """Gera um nome."""
    return FakeData().nome()

def cpf() -> str:
    """Gera um CPF."""
    return FakeData().cpf()

def email() -> str:
    """Gera um email."""
    return FakeData().email()

def telefone() -> str:
    """Gera um telefone."""
    return FakeData().telefone()

def endereco() -> str:
    """Gera um endereço."""
    return FakeData().endereco()

def data() -> str:
    """Gera uma data."""
    return FakeData().data_formatada()


# Função principal para demonstração
if __name__ == "__main__":
    print("=== FakeData - Geração de Dados Falsos ===\n")
    
    fake = FakeData(seed=42)  # Semente para reprodutibilidade
    
    # Nomes
    print("👤 Nomes:")
    print(f"  Nome: {fake.nome()}")
    print(f"  Primeiro nome (M): {fake.primeiro_nome(True)}")
    print(f"  Primeiro nome (F): {fake.primeiro_nome(False)}")
    print(f"  Sobrenome: {fake.sobrenome()}")
    
    # Documentos
    print("\n📋 Documentos:")
    print(f"  CPF: {fake.cpf()}")
    print(f"  CNPJ: {fake.cnpj()}")
    
    # Contato
    print("\n📞 Contato:")
    print(f"  Email: {fake.email()}")
    print(f"  Telefone: {fake.telefone()}")
    print(f"  Celular: {fake.celular()}")
    
    # Endereço
    print("\n🏠 Endereço:")
    print(f"  Endereço: {fake.endereco()}")
    print(f"  CEP: {fake.cep()}")
    print(f"  Cidade: {fake.cidade()}")
    print(f"  Estado: {fake.estado()}")
    
    # Data e Hora
    print("\n📅 Data e Hora:")
    print(f"  Data: {fake.data_formatada()}")
    print(f"  Hora: {fake.hora()}")
    print(f"  Data/Hora: {fake.data_hora()}")
    
    # Números e Texto
    print("\n🔢 Números e Texto:")
    print(f"  Número: {fake.numero(1, 100)}")
    print(f"  Decimal: {fake.decimal(0, 100)}")
    print(f"  Texto: {fake.texto(50)}")
    print(f"  Palavra: {fake.palavra(8)}")
    print(f"  Frase: {fake.frase(8)}")
    
    # Empresa
    print("\n🏢 Empresa:")
    print(f"  Empresa: {fake.empresa()}")
    print(f"  CNAE: {fake.cnae()}")
    print(f"  Produto: {fake.produto()}")
    print(f"  Preço: {fake.preco()}")
    
    # Cartão
    print("\n💳 Cartão:")
    print(f"  Número: {fake.numero_cartao()}")
    print(f"  Validade: {fake.validade_cartao()}")
    print(f"  CVV: {fake.cvv()}")
    
    # Pessoa completa
    print("\n👤 Pessoa Completa:")
    pessoa = fake.pessoa()
    for chave, valor in pessoa.items():
        print(f"  {chave}: {valor}")