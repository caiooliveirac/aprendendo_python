fact = int(input("Quer saber o fatorial de qual número? "))

razao = fact - 1

"""while razao > 0:
    fact = fact * razao
    razao -= 1
print(fact)"""

for i in range(fact-1):
    fact *= razao
    razao -= 1
print(fact)