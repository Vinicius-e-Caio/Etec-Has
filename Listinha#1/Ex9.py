import os
os.system("cls")

n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))
n3 = int(input("Valor 3: "))

if n1 > n2 and n1 > n3:
     print("{}".format(n1))

if n2 > n1 and n2 > n3:
     print("{}".format(n2))

if n3 > n2 and n3 > n1:
     print("{}".format(n3))