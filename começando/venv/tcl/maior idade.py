from datetime import date
atual = date.today().year
print("Estamos em {}".format(atual))
nascimentos = []
for i in range(1,8):
    data = int(input("Qual o seu ano de nascimento da {}ª pessoa?".format(i)))
    nascimentos.append(atual-data)

menores = []
maiores = []
for c in nascimentos:
    if c >= 18:
        maiores.append(c)
    else:
        menores.append(c)
print("Desse grupo, {} são maiores e {} são menores de idade.".format(len(maiores),len(menores)))