class Conta:
    codigo = 0
    saldo: 0.0

    def __init__(self, codigo, saldo=50):
        self.codigo = codigo
        self.saldo = saldo
    
    def imprimaSaldo(self):
        print("codigo: ", self.codigo, "saldo: ", self.saldo)
        
        if __name__ == '__main__':
            c1 = Conta(10,3240.52)
            c1.imprimaSaldo()
