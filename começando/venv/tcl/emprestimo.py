valor = float(input("Qual o valor do imóvel? "))
sal = float(input("Qual o seu salário mensal? "))
temp = float(input("Pretende pagar em quantos meses? "))

prest = valor / temp

if prest > (sal * 0.3):
    print("Este empréstimo excede o limite pré-aprovado. Experimente aumentar a entrada ou parcelar em menos tempo")
else:
    print("Seu empréstimo foi aprovado com parcelas de R${},00.".format(int(prest)))