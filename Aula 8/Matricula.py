estudante = {
    "nome": None,
    "nomeMae": None,
    "nomePai": None,
    "idade": None,
    "genero": None,
    "nacionalidade": None,
    "curso": None,
    "classe": None,
    "periodo": None,
}

def matricular():

    estudante["nome"] =   input("Digite o nome do estudante ")
    estudante["nomeMae"] =   input("Digite o nome da mãe ")
    estudante["nomePai"] =   input("Digite o nome do pai ")
    estudante["idade"] =  int(input("Digite a idade do estudante "))

    while(True):
        print("1- Masculino")
        print("2- Feminino")
        op = int(input("Escolha o genero: "))
        match op:
            case 1:
                estudante["genero"]  = "Masculino"
                break
            case 2:
                estudante["genero"] = "Femenino"
                break


    while(True):
        print("1- Angolano")
        print("2- Estrangeiro")
        op = int(input("Escolha o nacionalidade: "))
        match op:
            case 1:
                estudante["nacionalidade"] = "Angolano"
                break
            case 2:
                estudante["nacionalidade"] = "Estrangeiro"
                break


    while(True):
        print("1- Informatica")
        print("2- Recursos Humanos")
        print("3- Mecanica")
        op = int(input("Escolha o curso: "))
        match op:
            case 1:
                estudante["curso"] = "Informática"
                break
            case 2:
                estudante["curso"]  = "Recursos Humanos"
                break
            case 3:
                estudante["curso"]  = "Mecanica"
                break

    while(True):
        print("1- 10ª")
        print("2- 11ª")
        print("3- 12ª")
        print("4- 13ª")
        op = int(input("Escolha a classe: "))
        match op:
            case 1:
                estudante["classe"]  = "10"
                break
            case 2:
                estudante["classe"]  = "11"
                break
            case 3:
                estudante["classe"] = "12"
                break
            case 4:
                estudante["classe"] = "13"
                break

    while(True):
        print("1- Tarde")
        print("2- Manhã")
        print("3- Noite")
        op = int(input("Escolha o periodo: "))
        match op:
            case 1:
                estudante["periodo"] = "Tarde"
                break
            case 2:
                estudante["periodo"] = "Manhã"
                break
            case 3:
                estudante["periodo"] = "Noite"
                break

    salvar(estudante)

def salvar(novoEstudante):
    dados = novoEstudante["nome"]+","+novoEstudante["nomeMae"]+","+novoEstudante["nomePai"]+","+novoEstudante["genero"]+","+novoEstudante["nacionalidade"]+","+novoEstudante["curso"]+","+novoEstudante["periodo"]+"\n"
    with open('estudantes.txt','a+') as conteudo:
        conteudo.write(dados)


def listarEstudante(tag="todos"):
    just = False
    with open("estudantes.txt", "r") as arquivo:
        for linha in arquivo:
            estudante = linha.split(",")
            if(tag=="todos"):
                mostrarEstudante(estudante)
            elif(estudante[0].lower()==tag.lower()):
                print("Estudante encontrado ")
                mostrarEstudante(estudante)
                just= True
                break

def mostrarEstudante(estudante):
    print("------------------------------------")
    print("Nome do estudante: ",estudante[0])
    print("Nome da mãe: ",estudante[1])
    print("Nome do pai: ",estudante[2])
    print("Genero : ",estudante[3])
    print("Nacionalidade: ",estudante[4])
    print("Curso: ",estudante[5])
    print("Periodo: ",estudante[6])
