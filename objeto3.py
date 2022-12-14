class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        self.maiorlado= ""

    def calcularPerimetro(self):

        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro

    def getmaiorLado(self):
        if(self.ladoA > self.ladoB and self.ladoA >= self.ladoC):
            self.maiorlado = self.ladoA
        elif(self.ladoB >= self.ladoA and self.ladoB >= self.ladoC):
            self.maiorlado = self.ladoB
        elif(self.ladoC >= self.ladoA and self.ladoC >= self.ladoB):
            self.maiorlado = self.ladoC
        else:
            self.maiorlado = "Alguns lados são iguais."

triangulo1 = Triangulo(4,6,8)

print(triangulo1.calcularPerimetro())

triangulo1.getmaiorLado()
print(triangulo1.maiorlado)


