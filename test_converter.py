"""
Testes unitários para o módulo UnitConverter
"""

import pytest
from converter import UnitConverter


class TestUnitConverter:
    """Testes para a classe UnitConverter."""
    
    def setup_method(self):
        """Configuração antes de cada teste."""
        self.c = UnitConverter()
    
    # ========== COMPRIMENTO ==========
    
    def test_km_para_metros(self):
        """Testa conversão km → m."""
        assert self.c.comprimento(1, "km", "m") == 1000.0
    
    def test_polegadas_para_cm(self):
        """Testa conversão in → cm."""
        assert self.c.comprimento(12, "in", "cm") == pytest.approx(30.48, rel=1e-2)
    
    def test_milhas_para_km(self):
        """Testa conversão mi → km."""
        assert self.c.comprimento(1, "mi", "km") == pytest.approx(1609.344, rel=1e-2)
    
    def test_pe_para_metros(self):
        """Testa conversão ft → m."""
        assert self.c.comprimento(1, "ft", "m") == pytest.approx(0.3048, rel=1e-2)
    
    # ========== MASSA ==========
    
    def test_kg_para_gramas(self):
        """Testa conversão kg → g."""
        assert self.c.massa(1, "kg", "g") == 1000.0
    
    def test_libras_para_kg(self):
        """Testa conversão lb → kg."""
        assert self.c.massa(1, "lb", "kg") == pytest.approx(0.453592, rel=1e-2)
    
    def test_oncas_para_gramas(self):
        """Testa conversão oz → g."""
        assert self.c.massa(1, "oz", "g") == pytest.approx(28.3495, rel=1e-2)
    
    # ========== TEMPERATURA ==========
    
    def test_celsius_para_fahrenheit(self):
        """Testa conversão C → F."""
        assert self.c.temperatura(100, "C", "F") == 212.0
    
    def test_fahrenheit_para_celsius(self):
        """Testa conversão F → C."""
        assert self.c.temperatura(32, "F", "C") == 0.0
    
    def test_celsius_para_kelvin(self):
        """Testa conversão C → K."""
        assert self.c.temperatura(0, "C", "K") == 273.15
    
    def test_kelvin_para_celsius(self):
        """Testa conversão K → C."""
        assert self.c.temperatura(273.15, "K", "C") == 0.0
    
    def test_fahrenheit_para_kelvin(self):
        """Testa conversão F → K."""
        assert self.c.temperatura(32, "F", "K") == pytest.approx(273.15, rel=1e-2)
    
    # ========== VOLUME ==========
    
    def test_litro_para_ml(self):
        """Testa conversão L → mL."""
        assert self.c.volume(1, "L", "mL") == 1000.0
    
    def test_galao_para_litros(self):
        """Testa conversão gal → L."""
        assert self.c.volume(1, "gal", "L") == pytest.approx(3.78541, rel=1e-2)
    
    def test_xicara_para_ml(self):
        """Testa conversão cup → mL."""
        assert self.c.volume(1, "cup", "mL") == pytest.approx(236.588, rel=1e-2)
    
    # ========== VELOCIDADE ==========
    
    def test_kmh_para_ms(self):
        """Testa conversão km/h → m/s."""
        assert self.c.velocidade(100, "km/h", "m/s") == pytest.approx(27.7778, rel=1e-2)
    
    def test_mph_para_kmh(self):
        """Testa conversão mph → km/h."""
        assert self.c.velocidade(60, "mph", "km/h") == pytest.approx(96.5606, rel=1e-2)
    
    def test_nos_para_kmh(self):
        """Testa conversão kn → km/h."""
        assert self.c.velocidade(1, "kn", "km/h") == pytest.approx(1.852, rel=1e-2)
    
    # ========== ERROS ==========
    
    def test_unidade_invalida_comprimento(self):
        """Testa erro com unidade inválida."""
        with pytest.raises(ValueError):
            self.c.comprimento(1, "invalid", "m")
    
    def test_unidade_invalida_massa(self):
        """Testa erro com unidade inválida."""
        with pytest.raises(ValueError):
            self.c.massa(1, "kg", "invalid")
    
    def test_unidade_invalida_temperatura(self):
        """Testa erro com unidade inválida."""
        with pytest.raises(ValueError):
            self.c.temperatura(100, "C", "X")
    
    # ========== DETECÇÃO AUTOMÁTICA ==========
    
    def test_converter_automatico(self):
        """Testa detecção automática de categoria."""
        assert self.c.converter(1, "km", "m") == 1000.0
        assert self.c.converter(1, "kg", "g") == 1000.0
        assert self.c.converter(100, "C", "F") == 212.0
    
    # ========== LISTAR UNIDADES ==========
    
    def test_listar_unidades_comprimento(self):
        """Testa listagem de unidades de comprimento."""
        unidades = self.c.listar_unidades("comprimento")
        assert "m" in unidades
        assert "km" in unidades
        assert "ft" in unidades
    
    def test_listar_unidades_todas(self):
        """Testa listagem de todas as unidades."""
        unidades = self.c.listar_unidades()
        assert len(unidades) > 10


class TestFuncoesAuxiliares:
    """Testes para funções auxiliares."""
    
    def test_km_para_metros(self):
        """Testa função km_para_metros."""
        from converter import km_para_metros
        assert km_para_metros(1) == 1000.0
    
    def test_kg_para_gramas(self):
        """Testa função kg_para_gramas."""
        from converter import kg_para_gramas
        assert kg_para_gramas(1) == 1000.0
    
    def test_celsius_para_fahrenheit(self):
        """Testa função celsius_para_fahrenheit."""
        from converter import celsius_para_fahrenheit
        assert celsius_para_fahrenheit(100) == 212.0
    
    def test_fahrenheit_para_celsius(self):
        """Testa função fahrenheit_para_celsius."""
        from converter import fahrenheit_para_celsius
        assert fahrenheit_para_celsius(32) == 0.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])