a = []
for i in range(6):
    b = int(input("Me dê um número: "))
    a.append(b)
b= []
for c in a:
    if c % 2 == 0:
        b.append(c)
e = 0
for d in b:
    e += d

print(e)

