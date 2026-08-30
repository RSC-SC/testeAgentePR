"""
Módulo DateHandler - Manipulação de datas

Este módulo fornece uma classe para operações comuns com datas.
"""

from datetime import datetime, timedelta
from typing import Optional, Tuple


class DateHandler:
    """
    Classe para manipulação e operações com datas.
    
    Attributes:
        data: Data atual armazenada
        
    Examples:
        >>> handler = DateHandler()
        >>> print(handler.data_atual())
        2026-08-25
        >>> handler.adicionar_dias(7)
        >>> print(handler.data_atual())
        2026-09-01
    """
    
    def __init__(self, data_inicial: Optional[datetime] = None):
        """
        Inicializa o DateHandler.
        
        Args:
            data_inicial: Data inicial (opcional, padrão: data atual)
        """
        self.data = data_inicial or datetime.now()
    
    def data_atual(self) -> str:
        """
        Retorna a data atual formatada.
        
        Returns:
            Data no formato DD/MM/AAAA
            
        Examples:
            >>> handler = DateHandler()
            >>> handler.data_atual()
            '25/08/2026'
        """
        return self.data.strftime("%d/%m/%Y")
    
    def data_iso(self) -> str:
        """
        Retorna a data no formato ISO.
        
        Returns:
            Data no formato AAAA-MM-DD
            
        Examples:
            >>> handler = DateHandler()
            >>> handler.data_iso()
            '2026-08-25'
        """
        return self.data.strftime("%Y-%m-%d")
    
    def adicionar_dias(self, dias: int) -> datetime:
        """
        Adiciona dias à data atual.
        
        Args:
            dias: Número de dias a adicionar (pode ser negativo)
            
        Returns:
            Nova data
            
        Examples:
            >>> handler = DateHandler()
            >>> handler.adicionar_dias(10)
            datetime.datetime(2026, 9, 4, ...)
        """
        self.data += timedelta(days=dias)
        return self.data
    
    def subtrair_dias(self, dias: int) -> datetime:
        """
        Subtrai dias da data atual.
        
        Args:
            dias: Número de dias a subtrair
            
        Returns:
            Nova data
            
        Examples:
            >>> handler = DateHandler()
            >>> handler.subtrair_dias(5)
            datetime.datetime(2026, 8, 20, ...)
        """
        self.data -= timedelta(days=dias)
        return self.data
    
    def diferenca_dias(self, outra_data: datetime) -> int:
        """
        Calcula a diferença em dias entre duas datas.
        
        Args:
            otra_data: Outra data para comparar
            
        Returns:
            Número de dias de diferença
            
        Examples:
            >>> handler = DateHandler()
            >>> handler.diferenca_dias(datetime(2026, 12, 31))
            128
        """
        delta = outra_data - self.data
        return abs(delta.days)
    
    def eh_fim_de_semana(self) -> bool:
        """
        Verifica se a data atual é fim de semana.
        
        Returns:
            True se for sábado ou domingo
            
        Examples:
            >>> handler = DateHandler(datetime(2026, 8, 29))  # Sábado
            >>> handler.eh_fim_de_semana()
            True
        """
        return self.data.weekday() >= 5
    
    def dia_da_semana(self) -> str:
        """
        Retorna o nome do dia da semana.
        
        Returns:
            Nome do dia em português
            
        Examples:
            >>> handler = DateHandler(datetime(2026, 8, 25))
            >>> handler.dia_da_semana()
            'Segunda-feira'
        """
        dias = [
            "Segunda-feira", "Terça-feira", "Quarta-feira",
            "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
        ]
        return dias[self.data.weekday()]
    
    def proximo_dia_util(self) -> datetime:
        """
        Retorna o próximo dia útil.
        
        Returns:
            Próximo dia que não é fim de semana
            
        Examples:
            >>> handler = DateHandler(datetime(2026, 8, 29))  # Sábado
            >>> handler.proximo_dia_util()
            datetime.datetime(2026, 8, 31, ...)  # Segunda
        """
        proximo = self.data + timedelta(days=1)
        while proximo.weekday() >= 5:  # Pula fim de semana
            proximo += timedelta(days=1)
        return proximo
    
    def formatar(self, formato: str) -> str:
        """
        Formata a data conforme especificado.
        
        Args:
            formato: String de formato (ex: "%d/%m/%Y %H:%M")
            
        Returns:
            Data formatada
            
        Examples:
            >>> handler = DateHandler()
            >>> handler.formatar("%d/%m/%Y %H:%M")
            '25/08/2026 14:30'
        """
        return self.data.strftime(formato)
    
    def __str__(self) -> str:
        """Representação em string da data."""
        return self.data_atual()
    
    def __repr__(self) -> str:
        """Representação oficial do objeto."""
        return f"DateHandler(data='{self.data_iso()}')"


# Função auxiliar para criar DateHandler a partir de string
def parse_data(data_string: str, formato: str = "%d/%m/%Y") -> DateHandler:
    """
    Cria um DateHandler a partir de uma string.
    
    Args:
        data_string: String com a data
        formato: Formato da string (padrão: DD/MM/AAAA)
        
    Returns:
        DateHandler com a data parseada
        
    Examples:
        >>> handler = parse_data("25/12/2026")
        >>> print(handler.data_atual())
        '25/12/2026'
    """
    data = datetime.strptime(data_string, formato)
    return DateHandler(data)


# Função principal para demonstração
if __name__ == "__main__":
    print("=== DateHandler - Manipulação de Datas ===\n")
    
    # Criando handler com data atual
    handler = DateHandler()
    print(f"Data atual: {handler}")
    print(f"Formato ISO: {handler.data_iso()}")
    print(f"Dia da semana: {handler.dia_da_semana()}")
    print(f"É fim de semana? {handler.eh_fim_de_semana()}")
    
    # Operações com datas
    print(f"\nAdicionando 10 dias: {handler.adicionar_dias(10)}")
    print(f"Subtraindo 5 dias: {handler.subtrair_dias(5)}")
    
    # Próximo dia útil
    handler_proximo = DateHandler(datetime(2026, 8, 29))  # Sábado
    print(f"\nSábado 29/08/2026")
    print(f"Próximo dia útil: {handler_proximo.proximo_dia_util().strftime('%d/%m/%Y')}")
    
    # Diferença de datas
    data_fim = datetime(2026, 12, 31)
    handler_inicio = DateHandler()
    print(f"\nDias até 31/12/2026: {handler_inicio.diferenca_dias(data_fim)}")