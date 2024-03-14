import os
os.system("cls")

pol = int(input("Números de lados do polígono: "))

match pol:
        case 3:
                print("TRIÂNGULO")
                medidalado = int(input("Digite a medida(em cm) de um dos lados: "))
                valorarea = medidalado * 3
                print("Valor da área {}".format(valorarea))
        case 4:
                print("QUADRADO")
                medidalado = int(input("Digite a medida(em cm) de um dos lados: "))
                valorarea = medidalado * 4
                print("Valor da área {}".format(valorarea))
        case 5:
                print("PENTÁGONO")
                medidalado = int(input("Digite a medida(em cm) de um dos lados: "))
                valorarea = medidalado * 5
                print("Valor da área {}".format(valorarea))
        case _:
                print("Polígono invalido")