import os
os.system("cls")
import math

"""
    
    EXERCÍCIO:
Uma sala de aula tem 10 alunos.
A média semestral se dá pela média simples entre 3 notas, descartando
a de menor valor.
A cada nota digitada, verificar se ela está entre 0 e 10 (inclusive),
se não estiver exiba "Nota inválida" e peça para digitar novamente, caso
contrário, vá para a próxima nota.
No final, mostre a média da sala e quantos tiraram ao menos 9 de media.
    """

cont = 1
mediaAlu = 0
qntd = 0
keyNaN = 0

while cont <= 3:
    nota = 0
    menorNota = 0
    mediaFinal = 0
    mediaAlu = 0
    print(f"Aluno {cont}")
    for i in range(1,4,1):
       verify = False
       while verify == False:
          try:
                nota = float(input("\nDigite a nota do aluno no semestre:"))
          except:
                print("Algo deu errado.")
                keyNaN = 1
          
          if (nota <= 10 and nota >= 0 and keyNaN == 0):
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
              os.system("pause")
              os.system("cls")
       print(f"Nota {i} : {nota}")
        
    mediaFinal = (mediaAlu - menorNota) / 2
    if (mediaFinal >= 9):
        qntd = qntd + 1
    print(f"\n\nMedia final do aluno: {mediaFinal}")
    cont = cont + 1
    os.system("pause")
    os.system("cls")
    
print(f"Quantidade de alunos que tiraram 9 pra cima na média: {qntd}")



