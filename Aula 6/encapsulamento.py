class pessoa:
    def __init__(self,nome):
        self.__name = nome
    def getName(self):
        return self.__name

pessoa1 = pessoa("lukoki")

pessoa1 = pessoa("lukoki")
print(pessoa1.getName())