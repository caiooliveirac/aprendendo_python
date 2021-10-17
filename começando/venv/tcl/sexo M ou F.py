sexo = input("Qual o seu sexo? [M/F]: ")
while sexo not in "MFmf":
    sexo = input("Não corresponde as opções. Digite novamente por favor: ")
print("Entendi. O seu sexo é: {}.".format(sexo))


