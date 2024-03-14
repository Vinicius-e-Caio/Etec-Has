import os
from time import sleep
import math
os.system("cls")

sys = 0

while True:
     os.system("cls")

     print("""
     0 - Sair
     1 - Exercício 1
     2 - Exercício 2
     3 - Exercício 3
     4 - Exercício 4
     5 - Exercício 5
     6 - Exercício 6
     7 - Exercício 7
     8 - Exercício 8
     9 - Exercício 9
     10 - Exercício 10
     11 - Exercício 11
     12 - Exercício 12
     13 - Exercício 13
     14 - Exercício 14
          """)

     opcao = int(input("Escolha: "))

     match opcao:
          case 1:
               print("Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.")
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
               os.system("cls")
               n1 = int(input("Digite o primeiro valor: "))
               n2 = int(input("Digite o segundo valor: "))

               if n1 > n2:
                    print("O valor {} é o maior".format(n1))
               else:
                    print("O valor {} é o maior".format(n2))
               sleep(5) 
          case 2:
               print("Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).")
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
               os.system("cls")
               ano = int(input("Digite o ano que você nasceu: "))

               idade = 2024 - ano

               if idade >= 16:
                    print("Pode votar")
               else:
                    print("Não pode votar")
               sleep(5)
          case 3:
               print("""Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:
                    ACESSO PERMITIDO caso a senha seja válida.
                    ACESSO NEGADO caso a senha seja inválida.
                    """)
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
               os.system("cls")
               tentativa = int(input("Digite a senha: "))

               if tentativa == 1234:
                    print("ACESSO PERMITIDO")
               else:
                    print("ACESSO NEGADO")
               sleep(5)
          case 4:
               print("As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.")
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
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
               sleep(5)
          case 5:
               print("Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.")
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
               os.system("cls")
               num1 = int(input("Valor 1: "))
               num2 = int(input("Valor 2: "))
               num3 = int(input("Valor 3: "))

               if num1 > num2 and num1 > num3:
                    print("{}".format(num1))
                    if num2 > num3:
                         print("{}".format(num2))
                         print("{}".format(num3))
                    else:
                         print("{}".format(num3))
                         print("{}".format(num2))

               if num2 > num1 and num2 > num3:
                    print("{}".format(num2))
                    if num1 > num3:
                         print("{}".format(num1))
                         print("{}".format(num3))
                    else:
                         print("{}".format(num3))
                         print("{}".format(num1))

               if num3 > num2 and num3 > num1:
                    print("{}".format(num3))
                    if num1 > num2:
                         print("{}".format(num1))
                         print("{}".format(num2))
                    else:
                         print("{}".format(num2))
                         print("{}".format(num1))
               sleep(5)
          case 6:
               print("""Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes
                    Fórmulas:
                    - para homens: (72.7 * Altura) - 58
                    - para mulheres: (62.1* Altura) - 44.7
                    """)
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
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
               sleep(5)
          case 7:
               print("""
Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte:
     - Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
     - Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
               - Se o número de lados for igual a 5 escrever PENTÁGONO.
                     """)
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
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
               sleep(5)
          case 8:
               print("""
Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
     - Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
     - Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.""")
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
               os.system("cls")
               pol2 = int(input("Números de lados do polígono: "))

               match pol2:
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
                              if pol2 >= 5:
                                   print("Polígono não identificado")
                              elif pol2 < 3:
                                   print("Não é um polígono")
               sleep(5)
          case 9:
               print("Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário não informará valores iguais.")
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
               os.system("cls")
               nro1 = int(input("Valor 1: "))
               nro2 = int(input("Valor 2: "))
               nro3 = int(input("Valor 3: "))

               if nro1 > nro2 and nro1 > nro3:
                    print("{}".format(nro1))

               if nro2 > nro1 and nro2 > nro3:
                    print("{}".format(nro2))

               if nro3 > nro2 and nro3 > nro1:
                    print("{}".format(nro3))
               sleep(5)
          case 10:
               print("""
Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:
     - Triângulo Equilátero: possui os 3 lados iguais.
     - Triângulo Isóscele: possui 2 lados iguais.
     - Triângulo Escaleno: possui 3 lados diferentes.
                     """)
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
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
               sleep(5)
          case 11:
               print("""
Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
     - Triângulo Retângulo: possui um ângulo reto. (igual a 90°)
     - Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90°)
     - Triângulo Acutângulo: possui três ângulos agudos. (menor que 90°)
               """)
               sleep(0.5)
               print("A Cargar...")
               sleep(1.5)
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
               sleep(5)
          case 12:
                    fat = int(input("digite um número pára ver seu fatorial: "))
                    cont = fat - 1
                    while cont >= 1:
                         result = fat * cont
                         print("{} * {} = {}\n".format(fat, cont, result))
                         result = result + result
                         cont = cont - 1
          case 13:
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
          case 14:
               cont = 1
               mediaAlu = 0
               qntd = 0
               keyNaN = 0


               while cont <= 10:
                    nota = 0
                    menorNota = 0
                    mediaFinal = 0
                    mediaAlu = 0
                    print(f"Aluno {cont}")
                    for i in range(1,4,1):
                         verify = False
                         while verify == False:
                              nota = input("\nDigite a nota do aluno no semestre:")
                              if (math.isnan(nota)):
                                   keyNaN = 1
                              else:
                                   nota = float(nota)
                              if (nota <= 10 and nota >= 0 and keyNaN = 0):
                                   if (mediaAlu == 0):
                                        mediaAlu = mediaAlu + nota
                                        verify = True
                                        menorNota = nota
                                   elif (i == 2):
                                        if (menorNota >= nota):
                                             menorNota = nota
                                        mediaAlu = mediaAlu + nota
                                        verify = True
                                   else:
                                        if(menorNota >= nota):
                                             menorNota = nota
                                        mediaAlu = mediaAlu + nota
                                        verify = True
                                   
                              else:
                                   print("Nota inválida")
                         print(f"Nota {i} : {nota}")
                         
                    mediaFinal = (mediaAlu - menorNota) / 2
                    if (mediaFinal >= 9):
                         qntd = qntd + 1
                    print(f"\n\nMedia final do aluno: {mediaFinal}")
                    cont = cont + 1
                    os.system("pause")
                    os.system("cls")
               print(f"Quantidade de alunos que tiraram 9 pra cima na média: {qntd}")
               os.system("pause")
               os.system("cls")
          case 0:
               break
          case _:
               print("Opção invalida")
               sleep(2)


