numero = int(input("Diga o número: "))
divisores = []
print("O número é divisível por:", end=" ")
for i in range(1,19):
    if numero == 0:
        continue
    elif numero != i:
        if numero % i == 0:
            print(i,end=", ")
            divisores.append(i)

print(numero,end="")
print(".")

if len(divisores) < 2:
    print("Esse número é primo")

