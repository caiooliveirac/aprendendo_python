nome = 'Iolanda Dias Barbosa'
idade = '34'
ano_nasc = '1987'
conj = 'divorciada'

print("O que você quer saber sobre Iolanda? ")
var = input("")

if var.lower().strip() == "nome":
    print(nome)
elif var.lower().strip() == "idade":
    print(f"A idade de Iolanda é {idade} anos.")
elif var.find("conjugal") >= 0 or var.find("civil") >= 0:
    print(f"Iolanda é {conj}.")
elif "ano" in var.lower():
    print(f"Iolanda nasceu em {ano_nasc}.")
else:
    print("Não temos essa resposta!")
