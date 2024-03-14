import os
os.system("cls")

print("""
    É SÓ HOJE
    NA COMPRA 12 MAÇAS OU MAIS
    VOCÊ PAGA O,25 EM CADA!!!
      
    MENOS DISSO É 0,30
     """)

qntd = int(input("Qual a quantidade de maças?: "))

if qntd >= 12:
     total = qntd * 0.25
     print("O valor total é: {}".format(total))
else:
     total = qntd * 0.30
     print("O valor total é: R${:.2f}".format(total))
