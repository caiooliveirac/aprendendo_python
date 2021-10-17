import random

num = random.randint(1,5)

pac = int(input("Chute um número até 5: "))
if pac == num:
    print("Você acertou!!!")
else:
    print("ops! Errou feio, errou feio, errou rude!")