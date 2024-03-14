import os
os.system("cls")

#Estrutura de Decisão
# If simples
# # n = int(input("digite um numero:"))
# # if n < 0:
# #     n = -n

# # print("Numero: ",n)

#If Composto (if else)
# n = int(input("digite um numero:"))
# if n < 0:
#     print(f"O numero {n} é negativo")
# else:
#     print(f"O numero {n} NÃO é negativo")

#if Encadeado
# n = int(input("digite um numero:"))
# if n < 0:
#     print(f"O numero {n} é negativo")
# else:
#     if n > 0:
#         print("Positivo")
#     else:
#         print("Nulo")

#if - Elif
# n = int(input("digite um numero:"))
# if n < 0:
#     print("negativo")
# elif n > 0:
#     print("Positivo")
# elif n > 0:
#     print("Nulo")
# else:
#     print("NAN")

#if match case
print("""
1 - Exercício 1
2 - Exercício 2
3 - Exercício 3
4 - Exercicio 4
      """)
opcao = int(input("Escolha: "))
match opcao:
        case 1:
                print("Executando o Exercício 1")
        case 2:
                print("Executando o Exercício 2")
        case 3:
                print("Executando o Exercício 3")
        case 4:
                print("Executando o Exercício 4")
        case _:
                print("Opcao invalida")