import math

class Circulo:
    def __init__(self, radio):
        """
        Constructor de la clase Circulo.
        :param radio: Radio del circulo.
        """
        self.radio = radio
    
    def calcular_Area(self):
        return math.pi * self.radio ** 2
    
    def calcular_Circunferencia(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Circulo de radio {self.radio}"

mi_Circulo = Circulo(1000)
print(f"""
      {mi_Circulo}
      Área: {mi_Circulo.calcular_Area():.2f}
      Circunferencia: {mi_Circulo.calcular_Circunferencia():.2f}
      """)