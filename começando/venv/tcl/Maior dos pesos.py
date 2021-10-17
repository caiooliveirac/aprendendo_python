#lista = []
menor = 0
maior = 0
for i in range(1,6):
    pesos = int(input("Qual o peso da {}ª pessoa:".format(i)))
    if i == 1:
        maior = pesos
        menor = pesos
    if pesos >= maior:
        maior = pesos
    if pesos <= menor:
        menor = pesos

print("O mais pesado de todos é o que pesa {}Kg e o mais leve é o que pesa {}Kg.".format(maior,menor))
    #lista.append(pesos)

"""ordem = lista.sort()
op = lista[len(lista)-1]
ol = lista[0]
print("O mais pesado de todos é o que pesa {}Kg e o mais leve é o que pesa {}Kg.".format(op,ol))"""