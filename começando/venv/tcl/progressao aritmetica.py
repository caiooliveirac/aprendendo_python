primeiro = int(input("O primeiro termo: "))
razao = int(input("A razão: "))
numero_do_termo = int(input("Quer até qual termo da PA? "))
desejado = primeiro + razao * numero_do_termo


"""for i in range(primeiro,desejado,razao):
    print(i, end=" -> ")"""
i = 1
mais_termos = 1
print(primeiro,end=" ")
while i < numero_do_termo:
    primeiro += razao
    print(primeiro,end=" ")
    i += 1
print ("- pronto. Exibi {} termos.".format(numero_do_termo))

while mais_termos > 0:
    print()
    mais_termos = int(input("Deseja mais quantos termos? "))
    numero_do_termo += mais_termos
    while i < numero_do_termo:
        primeiro += razao
        print(primeiro,end=" ")
        i += 1
print("Terminamos então por aqui.")
