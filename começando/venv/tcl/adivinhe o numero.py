import random as rd
correto = rd.randint(1,60)
jogado = int(input("Chute um número: "))
tentativas = 1
print(correto)
while jogado != correto:
    jogado = int(input("Chute um número: "))
    tentativas += 1
print("Você acertou. A máquina havia pensado no número {}.".format(correto))
print("Você precisou de {} tentativas para acertar.".format(tentativas))