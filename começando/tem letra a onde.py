fras = input("Digite uma frase: ")

print("Essa frase contem {}x a letra a.".format(fras.count('a')))
print("Nessa frase a letra a aparece pela primeira vez na letra",fras.find('a')+1)
print("Nessa frase a letra a aparece pela ultima vez na letra",fras.rfind('a')+1)
