# Calcular o Fatorial de um numero
fat = int(input("digite um número pára ver seu fatorial: "))
cont = fat - 1
while cont >= 1:
    result = fat * cont
    print("{} * {} = {}\n".format(fat, cont, result))
    result = result + result
    cont = cont - 1