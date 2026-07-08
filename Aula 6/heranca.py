class Carros:
    def __init__(self,nome,cor):
        self.nome =nome
        self.cor = cor
    def descricao(self):
        print(f'o carro :{self.nome} é {self.cor}')

class leigo(Carros):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

leigo1 = leigo("yundai","amarela")
leigo2 = leigo("toyota","azul")

print(leigo1.descricao())
print(leigo2.descricao())

class Pessoa:
    def cadastrar(self,nome,idade):
        self.name = nome
        self.age = idade


pessoa1 = Pessoa()
pessoa2 = Pessoa()
pessoa1.cadastrar("Reciado",32)
pessoa2.cadastrar("Lukoki",35)

print(pessoa1.name,"Tem",pessoa1.age,"idade")
print(pessoa2.name,"Tem",pessoa2.age,"idade")