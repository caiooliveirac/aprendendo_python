nome = input("O nome: ")

if "silva" in nome.lower():
    print("Esse tem")

silv = nome.lower().find("silva")
if silv > -1:
    print ("Esse nome contem Silva")
else:
    print("Esse não é da família Silva")