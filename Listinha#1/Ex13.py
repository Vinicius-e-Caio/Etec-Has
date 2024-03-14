# # Processar qual o próximo primo a partir de um número
# num = int(input("Digite um número para ver seu próximo primo: "))
# num = num + 1
# cont = 1
# while cont > 0:
#       if num % 3 == 0:
#           print("O próximo número primo é: {}".format(num))
#           cont = 0
#       else:
#           num = num + 1

num = int(input("Digite um número: "))
num = num + 1
cont = 2
while cont > 1:
    if num == 3:
        print("O Número primo mais próximo é 3")
        cont = 0
    else:
        if num % 3 != 0:
            print(f"o número primo mais próximo é:{num}")
            cont = 0
        else:
            num = num + 1