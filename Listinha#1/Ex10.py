import os
os.system("cls")

med1 = float(input("Valor 1: "))
med2 = float(input("Valor 2: "))
med3 = float(input("Valor 3: "))

if med1 != med2 and med1 != med3 and med2 != med3:
     print("É Escaleno")
elif med1 == med2 and med1 == med3 and med2 == med3:
     print("É Equilátero")
else:
     print("É Isóscele") 