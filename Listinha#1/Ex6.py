import os
os.system("cls")

print("""
1 - Feminino
2 - Masculino
      """)
sexo = int(input("Escolha: "))
match sexo:
        case 1:
                alt = float(input("Digite sua altura: "))
                pesoideal = (72.7 * alt) - 58
                print("Seu peso ideal é {}".format(pesoideal))
        case 2:
                alt = float(input("Digite sua altura: "))
                pesoideal = (62.1 * alt) - 44.7
                print("Seu peso ideal é {}".format(pesoideal))
        case _:
                print("Sexo invalido")