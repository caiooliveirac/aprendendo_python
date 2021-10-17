import random

veloc = random.randint(20,150)

if veloc > 80:
    print("Você passou aqui a {}km/h".format(veloc))
    print("Vai ter que pagar uma multa de R${},00".format(int((veloc-80)*0.7)))
else:
    print("Passou aqui a {}km/h".format(veloc))