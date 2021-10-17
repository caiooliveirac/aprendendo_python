print("="*20+"TABELA DEMOGRÁFICA"+"="*20)
num_pessoas = int(input("Quantas pessoas no grupo?"))
o_mais_velho = ""
idade_do_mais_velho = 0
idades = 0
menor_de_vinte = 0
for i in range(1,num_pessoas+1):
    nome = input("Qual o nome do {}º integrante?".format(i))
    idade = int(input("Qual idade do {}º integrante?".format(i)))
    idades += idade
    sexo = input("Qual o sexo do {}º integrante?".format(i))
    if sexo.lower() == ("m" or 'masculino') and o_mais_velho == "":
        o_mais_velho = nome
        idade_do_mais_velho = idade
        print("pegou esse")
    if idade > idade_do_mais_velho and sexo.lower() in "masculino":
        idade_do_mais_velho = idade
        o_mais_velho = nome
        print("pegou o de cá")
    if sexo.lower() == "feminino" and idade < 20:
        menor_de_vinte += 1
    print(o_mais_velho)
    print(sexo,sexo.lower())

print("A média das idades é de {} anos.".format(idades/num_pessoas))
print("O homem mais velho é o {}".format(o_mais_velho))
print("O número de mulheres menores de 20 anos é {}.".format(menor_de_vinte))