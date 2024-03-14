import os
os.system("cls")

ang1 = int(input("Valor 1: "))
ang2 = int(input("Valor 2: "))
ang3 = int(input("Valor 3: "))

somatotal = ang1 + ang2 + ang3

if somatotal == 90:
     print("Triângulo Retângulo")
elif somatotal > 90:
     print("Triângulo Obtusângulo")
elif somatotal < 90:
     print("Triângulo Acutângulo")
