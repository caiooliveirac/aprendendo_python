numer = 0
quantos = 0
soma = 0
while numer != 999:
    numer = int(input("Digite um número qualquer. Digitar 999 encerra o programa: "))
    if numer != 999:
        soma += numer
        quantos += 1
print("Ok. Encerrando. Você digitou {} números. A soma de todos eles seria {}.".format(quantos,soma))
