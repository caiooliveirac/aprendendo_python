fibo = int(input("Me diga até qual posição quer a sequência de Fibo: "))
i= 3

numfib = 1
antecess = 0

print(antecess,numfib,end=" ")
while i <= fibo:
    j = numfib + antecess
    print(j,end=" ")
    antecess = numfib
    numfib = j
    i += 1
