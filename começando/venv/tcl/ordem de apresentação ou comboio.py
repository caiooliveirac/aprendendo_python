import random
list = []
for i in range(4):
    alun = input("Me diga o nome do aluno: ")
    list.append(alun)

for i in range(4):
    numer = random.randint(0,len(list)-1)
    sort = list[numer]
    print(sort)
    list.pop(numer)