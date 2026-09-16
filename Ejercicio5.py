class PEscritorio:
    def prueba1(self, suma, x):
        self.suma = suma
        self.x = x
        self.suma = self.suma + self.x
        return self.suma
    def prueba2(self, y):
        self.y = y
        self.x = self.x + (self.y ** 2)
        return self.x
    def prueba3(self):
        self.suma = self.suma + (self.x / self.y)
        return self.suma
escritorio = PEscritorio()
print(escritorio.prueba1(0, 20))    
print(escritorio.prueba2(40))       
print("EL VALOR DE LA SUMA ES:", escritorio.prueba3())  