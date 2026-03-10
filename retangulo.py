class Retangulo:
    base = 0.0
    altura = 0.0
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura 

    def getArea(self):
        return self.base * self.altura
    
    def getPerimetro(self):
        return 2 * (self.base + self.altura)
    
    def Descricao(self):
        print("=== Dados do Retângulo ===")
        print("Base: ", self.base)
        print("Altura: ", self.altura)
        print("Área: ", self.getArea())
        print("Perímetro: ", self.getPerimetro())

ret = Retangulo(10, 5)

ret.Descricao()