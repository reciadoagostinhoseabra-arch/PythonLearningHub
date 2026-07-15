import os
import Matricula

while(True):
    try:
        print("----------------------------------------")
        print("1- MATRICULAR ESTUDANTE")
        print("2- LISTAR ESTUDANTE")
        print("3- ELIMINAR ESTUDATE")
        print("4- CADASTRAR PROFESSOR")
        print("5- LISTAR PROFESSOR")
        print("6- ELIMINAR PROFESSOR")
        print("7- PESQUISAR ESTUDANTE")
        print("8- PESQUISAR PROFESSOR")
        print("0- SAIR")
        print("----------------------------------------")
        opcao = int(input("Escolha uma opcão: "))
        match opcao:
            case 1:
                print("TELA MATRICULAR ESTUDANTE")
                Matricula.matricular()
                os.system("clear")
            case 2:
                print("TELA LISTAR ESTUDANTE")
                Matricula.mostrar()
            case 3:
                print("TELA ELIMINAR ESTUDANTE")
                os.system("clear")
            case 4:
                print("TELA CADASTRAR PROFESSOR")
                os.system("clear")
            case 5:
                print("TELA LISTAR PROFESSOR")
                os.system("clear")
            case 6:
                print("TELA ELIMINAR PROFESSOR")
                os.system("clear")
            case 7:
                print("TELA PESQUISAR ESTUDANTE")
                os.system("clear")
            case 8:
                print("TELA PESQUISAR PROFESSOR")
                os.system("clear")
            case 0:
                print("Volte sempre")
                break
                os.system("clear")
            case _:
                print("opcão invalida")
    except:
        print("A opcão deve ser umvalor inteiro")