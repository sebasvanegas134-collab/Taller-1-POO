class Potencias:
    def __init__(self,N):
        self.N = N
        self.cuadrado = N ** 2
        self.cubo = N ** 3
        return 
numero = Potencias(float(input()))
print(numero.cuadrado)
print(numero.cubo)