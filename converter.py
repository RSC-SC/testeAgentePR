"""
Módulo UnitConverter - Conversão de unidades

Este módulo fornece funções para conversão entre diferentes unidades de medida.
"""

from typing import Optional, Dict, Tuple


class UnitConverter:
    """
    Classe para conversão de unidades de medida.
    
    Supports:
        - Comprimento: metro, quilômetro, centímetro, milímetro, pé, polegada
        - Massa: quilograma, grama, libra, onça
        - Temperatura: Celsius, Fahrenheit, Kelvin
        - Volume: litro, mililitro, galão, xícara
        - Velocidade: km/h, m/s, mph, nós
    
    Examples:
        >>> converter = UnitConverter()
        >>> converter.comprimento(1, "km", "m")
        1000.0
        >>> converter.temperatura(100, "C", "F")
        212.0
    """
    
    # Fatores de conversão para comprimento (base: metro)
    COMPRIMENTO: Dict[str, float] = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "ft": 0.3048,
        "in": 0.0254,
        "mi": 1609.344,
        "yd": 0.9144,
    }
    
    # Fatores de conversão para massa (base: quilograma)
    MASSA: Dict[str, float] = {
        "kg": 1.0,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495,
        "t": 1000.0,
    }
    
    # Fatores de conversão para volume (base: litro)
    VOLUME: Dict[str, float] = {
        "L": 1.0,
        "mL": 0.001,
        "gal": 3.78541,
        "cup": 0.236588,
        "fl_oz": 0.0295735,
        "tbsp": 0.0147868,
        "tsp": 0.00492892,
    }
    
    # Fatores de conversão para velocidade (base: km/h)
    VELOCIDADE: Dict[str, float] = {
        "km/h": 1.0,
        "m/s": 3.6,
        "mph": 1.60934,
        "kn": 1.852,
        "ft/s": 1.09728,
    }
    
    # Nomes completos das unidades
    NOMES: Dict[str, str] = {
        "m": "metro",
        "km": "quilômetro",
        "cm": "centímetro",
        "mm": "milímetro",
        "ft": "pé",
        "in": "polegada",
        "mi": "milha",
        "yd": "jarda",
        "kg": "quilograma",
        "g": "grama",
        "mg": "miligrama",
        "lb": "libra",
        "oz": "onça",
        "t": "tonelada",
        "L": "litro",
        "mL": "mililitro",
        "gal": "galão",
        "cup": "xícara",
        "fl_oz": "onça fluida",
        "tbsp": "colher de sopa",
        "tsp": "colher de chá",
        "km/h": "quilômetro por hora",
        "m/s": "metro por segundo",
        "mph": "milha por hora",
        "kn": "nó",
        "ft/s": "pé por segundo",
        "C": "Celsius",
        "F": "Fahrenheit",
        "K": "Kelvin",
    }
    
    def __init__(self):
        """Inicializa o UnitConverter."""
        pass
    
    def _converter_fator(self, valor: float, de_fator: float, para_fator: float) -> float:
        """
        Converte usando fatores de conversão.
        
        Args:
            valor: Valor a ser convertido
            de_fator: Fator de conversão da unidade origem
            para_fator: Fator de conversão da unidade destino
            
        Returns:
            Valor convertido
        """
        # Converter para unidade base, depois para unidade destino
        valor_base = valor * de_fator
        return valor_base / para_fator
    
    def comprimento(self, valor: float, de: str, para: str) -> float:
        """
        Converte unidades de comprimento.
        
        Args:
            valor: Valor a ser convertido
            de: Unidade de origem
            para: Unidade de destino
            
        Returns:
            Valor convertido
            
        Raises:
            ValueError: Se as unidades não forem suportadas
            
        Examples:
            >>> converter = UnitConverter()
            >>> converter.comprimento(1, "km", "m")
            1000.0
            >>> converter.comprimento(12, "in", "cm")
            30.48
        """
        de = de.lower()
        para = para.lower()
        
        if de not in self.COMPRIMENTO:
            raise ValueError(f"Unidade '{de}' não suportada. Use: {list(self.COMPRIMENTO.keys())}")
        if para not in self.COMPRIMENTO:
            raise ValueError(f"Unidade '{para}' não suportada. Use: {list(self.COMPRIMENTO.keys())}")
        
        return self._converter_fator(valor, self.COMPRIMENTO[de], self.COMPRIMENTO[para])
    
    def massa(self, valor: float, de: str, para: str) -> float:
        """
        Converte unidades de massa.
        
        Args:
            valor: Valor a ser convertido
            de: Unidade de origem
            para: Unidade de destino
            
        Returns:
            Valor convertido
            
        Examples:
            >>> converter = UnitConverter()
            >>> converter.massa(1, "kg", "g")
            1000.0
            >>> converter.massa(1, "lb", "kg")
            0.453592
        """
        de = de.lower()
        para = para.lower()
        
        if de not in self.MASSA:
            raise ValueError(f"Unidade '{de}' não suportada. Use: {list(self.MASSA.keys())}")
        if para not in self.MASSA:
            raise ValueError(f"Unidade '{para}' não suportada. Use: {list(self.MASSA.keys())}")
        
        return self._converter_fator(valor, self.MASSA[de], self.MASSA[para])
    
    def volume(self, valor: float, de: str, para: str) -> float:
        """
        Converte unidades de volume.
        
        Args:
            valor: Valor a ser convertido
            de: Unidade de origem
            para: Unidade de destino
            
        Returns:
            Valor convertido
            
        Examples:
            >>> converter = UnitConverter()
            >>> converter.volume(1, "L", "mL")
            1000.0
            >>> converter.volume(1, "gal", "L")
            3.78541
        """
        de = de.lower()
        para = para.lower()
        
        if de not in self.VOLUME:
            raise ValueError(f"Unidade '{de}' não suportada. Use: {list(self.VOLUME.keys())}")
        if para not in self.VOLUME:
            raise ValueError(f"Unidade '{para}' não suportada. Use: {list(self.VOLUME.keys())}")
        
        return self._converter_fator(valor, self.VOLUME[de], self.VOLUME[para])
    
    def velocidade(self, valor: float, de: str, para: str) -> float:
        """
        Converte unidades de velocidade.
        
        Args:
            valor: Valor a ser convertido
            de: Unidade de origem
            para: Unidade de destino
            
        Returns:
            Valor convertido
            
        Examples:
            >>> converter = UnitConverter()
            >>> converter.velocidade(100, "km/h", "m/s")
            27.7778
        """
        de = de.lower()
        para = para.lower()
        
        if de not in self.VELOCIDADE:
            raise ValueError(f"Unidade '{de}' não suportada. Use: {list(self.VELOCIDADE.keys())}")
        if para not in self.VELOCIDADE:
            raise ValueError(f"Unidade '{para}' não suportada. Use: {list(self.VELOCIDADE.keys())}")
        
        return self._converter_fator(valor, self.VELOCIDADE[de], self.VELOCIDADE[para])
    
    def temperatura(self, valor: float, de: str, para: str) -> float:
        """
        Converte unidades de temperatura.
        
        Args:
            valor: Valor a ser convertido
            de: Unidade de origem (C, F, K)
            para: Unidade de destino (C, F, K)
            
        Returns:
            Valor convertido
            
        Examples:
            >>> converter = UnitConverter()
            >>> converter.temperatura(100, "C", "F")
            212.0
            >>> converter.temperatura(0, "F", "C")
            -17.7778
        """
        de = de.upper()
        para = para.upper()
        
        unidades_validas = ["C", "F", "K"]
        
        if de not in unidades_validas:
            raise ValueError(f"Unidade '{de}' não suportada. Use: {unidades_validas}")
        if para not in unidades_validas:
            raise ValueError(f"Unidade '{para}' não suportada. Use: {unidades_validas}")
        
        # Converter para Celsius primeiro
        if de == "C":
            celsius = valor
        elif de == "F":
            celsius = (valor - 32) * 5 / 9
        else:  # K
            celsius = valor - 273.15
        
        # Converter de Celsius para unidade destino
        if para == "C":
            return celsius
        elif para == "F":
            return celsius * 9 / 5 + 32
        else:  # K
            return celsius + 273.15
    
    def converter(self, valor: float, de: str, para: str, categoria: str = None) -> float:
        """
        Converte entre unidades (detecta categoria automaticamente).
        
        Args:
            valor: Valor a ser convertido
            de: Unidade de origem
            para: Unidade de destino
            categoria: Categoria opcional (comprimento, massa, etc.)
            
        Returns:
            Valor convertido
            
        Examples:
            >>> converter = UnitConverter()
            >>> converter.converter(1, "km", "m")
            1000.0
        """
        de_lower = de.lower()
        para_lower = para.lower()
        
        # Tentar detectar categoria automaticamente
        if de_lower in self.COMPRIMENTO and para_lower in self.COMPRIMENTO:
            return self.comprimento(valor, de, para)
        elif de_lower in self.MASSA and para_lower in self.MASSA:
            return self.massa(valor, de, para)
        elif de_lower in self.VOLUME and para_lower in self.VOLUME:
            return self.volume(valor, de, para)
        elif de_lower in self.VELOCIDADE and para_lower in self.VELOCIDADE:
            return self.velocidade(valor, de, para)
        elif de.upper() in ["C", "F", "K"] and para.upper() in ["C", "F", "K"]:
            return self.temperatura(valor, de, para)
        else:
            raise ValueError(f"Não foi possível detectar categoria para {de} → {para}")
    
    def listar_unidades(self, categoria: str = None) -> Dict[str, str]:
        """
        Lista unidades disponíveis.
        
        Args:
            categoria: Categoria específica (opcional)
            
        Returns:
            Dicionário com código e nome da unidade
        """
        if categoria == "comprimento":
            return {k: self.NOMES.get(k, k) for k in self.COMPRIMENTO.keys()}
        elif categoria == "massa":
            return {k: self.NOMES.get(k, k) for k in self.MASSA.keys()}
        elif categoria == "volume":
            return {k: self.NOMES.get(k, k) for k in self.VOLUME.keys()}
        elif categoria == "velocidade":
            return {k: self.NOMES.get(k, k) for k in self.VELOCIDADE.keys()}
        elif categoria == "temperatura":
            return {"C": "Celsius", "F": "Fahrenheit", "K": "Kelvin"}
        else:
            # Retornar todas
            todas = {}
            todas.update(self.COMPRIMENTO)
            todas.update(self.MASSA)
            todas.update(self.VOLUME)
            todas.update(self.VELOCIDADE)
            todas["C"] = "Celsius"
            todas["F"] = "Fahrenheit"
            todas["K"] = "Kelvin"
            return {k: self.NOMES.get(k, k) for k in todas.keys()}


# Funções auxiliares para uso rápido
def km_para_metros(km: float) -> float:
    """Converte quilômetros para metros."""
    return UnitConverter().comprimento(km, "km", "m")


def kg_para_gramas(kg: float) -> float:
    """Converte quilogramas para gramas."""
    return UnitConverter().massa(kg, "kg", "g")


def celsius_para_fahrenheit(celsius: float) -> float:
    """Converte Celsius para Fahrenheit."""
    return UnitConverter().temperatura(celsius, "C", "F")


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    """Converte Fahrenheit para Celsius."""
    return UnitConverter().temperatura(fahrenheit, "F", "C")


# Função principal para demonstração
if __name__ == "__main__":
    print("=== UnitConverter - Conversão de Unidades ===\n")
    
    c = UnitConverter()
    
    # Comprimento
    print("📏 Comprimento:")
    print(f"  1 km = {c.comprimento(1, 'km', 'm')} metros")
    print(f"  12 polegadas = {c.comprimento(12, 'in', 'cm')} cm")
    print(f"  1 milha = {c.comprimento(1, 'mi', 'km')} km")
    
    # Massa
    print("\n⚖️  Massa:")
    print(f"  1 kg = {c.massa(1, 'kg', 'g')} gramas")
    print(f"  1 libra = {c.massa(1, 'lb', 'kg')} kg")
    
    # Temperatura
    print("\n🌡️  Temperatura:")
    print(f"  100°C = {c.temperatura(100, 'C', 'F')}°F")
    print(f"  32°F = {c.temperatura(32, 'F', 'C')}°C")
    print(f"  0°C = {c.temperatura(0, 'C', 'K')} K")
    
    # Volume
    print("\n🧪 Volume:")
    print(f"  1 galão = {c.volume(1, 'gal', 'L')} litros")
    print(f"  1 xícara = {c.volume(1, 'cup', 'mL')} mL")
    
    # Velocidade
    print("\n🚗 Velocidade:")
    print(f"  100 km/h = {c.velocidade(100, 'km/h', 'm/s')} m/s")
    print(f"  60 mph = {c.velocidade(60, 'mph', 'km/h')} km/h")
    
    # Listar unidades
    print("\n📋 Unidades disponíveis (comprimento):")
    for codigo, nome in c.listar_unidades("comprimento").items():
        print(f"  {codigo}: {nome}")