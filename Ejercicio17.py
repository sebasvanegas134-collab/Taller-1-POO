import math
class Circulo:
    def __init__(self,radio):
        self.radio = radio
        self.area = math.pi * radio**2
        self.perimetro = math.pi * radio * 2
Radio = Circulo(float(input()))
print(Radio.area) 
print(Radio.perimetro)   