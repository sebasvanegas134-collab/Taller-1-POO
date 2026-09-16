class edades:
    def __init__(self,edad):
        self.edad = edad
    def alberto(self):
        EdaDA = self.edad * 2/3
        EdaDA = round(EdaDA)
        return EdaDA
    def ana(self):
        EdaDAN = self.edad * 4/3
        EdaDAN = round(EdaDAN)
        return EdaDAN
    def mama(self):
        EdaDM = self.ana() + self.alberto() + self.edad
        return EdaDM
    
EdaDJ = edades(int(input()))
Alberto = EdaDJ.alberto()
Ana = EdaDJ.ana()
Mama = EdaDJ.mama()

print(Alberto)
print(Ana)
print(Mama)
