class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    def print(self):
        print("***************")
        print("NOME:"+self.nome)
        print("CPF: "+self.cpf)
        print("***************")

if __name__ == '__main__':
    pessoa1 = Pessoa("Mathias", '948.344.534-93')
    pessoa2 = Pessoa("José", '356.645.655-33')
    pessoa3 = Pessoa("Maria", '222.666.444-99')
    pessoa4 = Pessoa("João", '444.334.557-98')

    pessoa1.print()
    pessoa2.print()
    pessoa3.print()
    pessoa4.print()