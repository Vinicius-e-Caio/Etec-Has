#2 dado os dias de vida de um usuário, informar quantos anos, meses, e dias de vida ele tem

entrada = int(input("quantos dias de vida você tem"))
anos = entrada // 365
dias_restantes = entrada % 365
meses = dias_restantes // 30
dias = dias_restantes % 30

print("{} anos {} meses {} dias".format(anos,meses,dias))