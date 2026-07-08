class Carros:
    def __init__(self,nome,cor):
        self.nome =nome
        self.cor = cor
    def descricao(self):
        print(f'o carro :{self.nome} é {self.cor}')

class leigo(Carros):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)


class leiga(Carros):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def descricao(self,tipo):
        print(f'o carro :{self.nome} é {self.cor} e tipo {tipo}')


leigo1 = leigo("yundai","azul")
leiga1 = leiga("toyote","amarela")

print(leigo1.descricao())
print(leiga1.descricao("estragado"))

