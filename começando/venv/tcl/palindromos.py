palin = input("Que palavra quer testar? ")
letras = []

for i in palin:
   letras.append(i)
invertido = letras[::-1]

invers = []

for c in range(len(letras))[::-1]:
    item = letras[c]
    invers.append(item)


nome_invertido = "".join(invers)
print("Invertendo as letras dessa palavra, temos:",nome_invertido)

if nome_invertido.lower() == palin.lower():
    print("Sim, é um palíndromo.")
else:
    print("Como você pode ver, não temos um palíndromo!")