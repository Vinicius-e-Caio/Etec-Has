import os
os.system("cls")

ano = int(input("Digite o ano que você nasceu: "))

idade = 2024 - ano

if idade >= 16:
     print("Pode votar")
else:
     print("Não pode votar")