"""
Testes unitários para o módulo DateHandler
"""

import pytest
from datetime import datetime
from date_handler import DateHandler, parse_data


class TestDateHandler:
    """Testes para a classe DateHandler."""
    
    def test_data_atual(self):
        """Testa se a data atual é retornada corretamente."""
        handler = DateHandler()
        data = handler.data_atual()
        assert len(data) == 10  # DD/MM/AAAA
        assert "/" in data
    
    def test_data_iso(self):
        """Testa se a data ISO é retornada corretamente."""
        handler = DateHandler()
        data = handler.data_iso()
        assert len(data) == 10  # AAAA-MM-DD
        assert "-" in data
    
    def test_adicionar_dias(self):
        """Testa adição de dias."""
        handler = DateHandler(datetime(2026, 8, 25))
        handler.adicionar_dias(10)
        assert handler.data.day == 4
        assert handler.data.month == 9
    
    def test_subtrair_dias(self):
        """Testa subtração de dias."""
        handler = DateHandler(datetime(2026, 8, 25))
        handler.subtrair_dias(5)
        assert handler.data.day == 20
    
    def test_diferenca_dias(self):
        """Testa cálculo de diferença em dias."""
        handler = DateHandler(datetime(2026, 8, 25))
        outra_data = datetime(2026, 12, 31)
        assert handler.diferenca_dias(outra_data) == 128
    
    def test_eh_fim_de_semana(self):
        """Testa verificação de fim de semana."""
        # Sábado
        handler_sabado = DateHandler(datetime(2026, 8, 29))
        assert handler_sabado.eh_fim_de_semana() is True
        
        # Segunda
        handler_segunda = DateHandler(datetime(2026, 8, 25))
        assert handler_segunda.eh_fim_de_semana() is False
    
    def test_dia_da_semana(self):
        """Testa retorno do dia da semana."""
        handler = DateHandler(datetime(2026, 8, 25))  # Segunda
        assert handler.dia_da_semana() == "Segunda-feira"
    
    def test_proximo_dia_util(self):
        """Testa busca do próximo dia útil."""
        # Sábado
        handler = DateHandler(datetime(2026, 8, 29))
        proximo = handler.proximo_dia_util()
        assert proximo.weekday() == 0  # Segunda
    
    def test_formatar(self):
        """Testa formatação customizada."""
        handler = DateHandler(datetime(2026, 8, 25, 14, 30))
        assert handler.formatar("%d/%m/%Y %H:%M") == "25/08/2026 14:30"
    
    def test_str(self):
        """Testa representação em string."""
        handler = DateHandler(datetime(2026, 8, 25))
        assert str(handler) == "25/08/2026"
    
    def test_repr(self):
        """Testa representação oficial."""
        handler = DateHandler(datetime(2026, 8, 25))
        assert "DateHandler" in repr(handler)


class TestParseData:
    """Testes para a função parse_data."""
    
    def test_parse_data_padrao(self):
        """Testa parse com formato padrão."""
        handler = parse_data("25/12/2026")
        assert handler.data.day == 25
        assert handler.data.month == 12
        assert handler.data.year == 2026
    
    def test_parse_data_formato_customizado(self):
        """Testa parse com formato customizado."""
        handler = parse_data("2026-08-25", "%Y-%m-%d")
        assert handler.data.day == 25


if __name__ == "__main__":
    pytest.main([__file__, "-v"])