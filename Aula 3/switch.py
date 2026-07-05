n = (int)(input("Digite um numero de 1 ate 5 "))

match n:
    case 1:
        print("vc digitou o numero 1")
    case 2:
        print("vc digitou o numero 2")
    case 3:
        print("vc digitou o numero 3")
    case _:
        print("numero não previsto")
