## Comentario de uma linha

'''
Jesus
'''

"""
Hello World
"""

# Saida de dados | print() ~ printf()
print("Hello World")

# Variávais em Phyton não são tipadas
x = 10
print(x, type(x))

x = 10.5
print(x, type(x))

x = "2BI"
print(x, type(x))

x = True
print(x, type(x))

# Tipos em Phyton
"""
int - inteiro
float - real
str - string | Texto
bool - Lógico
"""

# Casting - Ato de mudar o tipo da variável via código
"""
int()
float()
str()
bool()
"""

x = 25
x = bool(x)
print(x, type(x))

# Entrada de dados - input() ~ scanf()
# O input sempre lê dados str
valor1 = int(input("Digite o 1ro numero:"))
valor2 = int(input("Digite o 2ro numero:"))
resposta = valor1 + valor2
print("Resposta: ", resposta)

#Formatações
texto = "Edson"
valor = 23
salario = 1234.56
filhos = True
print("Boa tarde " + texto)
print("Boa tarde" , texto)
print("Valor =" , valor)
print("Nome {} {}".format(texto, valor))
print("Nome {1} {0}".format(texto, valor))
print("Nome {0} - {1} - {2} - {3}".format(texto, valor, salario, filhos))
print("Salario: {0} ".format(salario))
print("Salario: {0:.3f} ".format(salario))
print("Salario: {0:.4f} ".format(salario))
print("Salario: {0:.2f} ".format(salario))
print("Salario: {0:10.2f} ".format(salario))
print("Salario: {0:8.2f} ".format(salario))
print("Salario: {0:5} ".format(salario))
print("Salario: {0:05} ".format(salario))

# Formatação com print(f)
print("Oi")
print('Oi')
nome = "Edson de Oliveira"
idade = 49
salario = 45645.65
print(f"Nome: {nome} \nidade: {idade} \nsalario: {salario}")
print(f"""
Nome: {nome}
idade: {idade:05}
salario {salario:10.3f}
""")

# Operadores aritméticos
valor1 = 10
valor2 = 3
resposta = 10 + 3 #soma
print(f"Resposta: {resposta}")
resposta = 10 - 3 #subtração
print(f"Resposta: {resposta}")
resposta = 10 * 3 #multiplicação
print(f"Resposta: {resposta}")
resposta = 10 / 3 #divisão
print(f"Resposta: {resposta}")
resposta = 10 // 3 #divisão inteira
print(f"Resposta: {resposta}")
resposta = 10 ** 3 #exponenciação (dez ao cubo)
print(f"Resposta: {resposta}")
resposta = 10 % 3 #módulo / resto
print(f"Resposta: {resposta}")
resposta = 10 % 3.5 #módulo / resto
print(f"Resposta: {resposta}")
resposta = 10 % 3.7                                                                                                                                                                                                                                                                                                                            #módulo / resto
print(f"Resposta: {resposta}")
