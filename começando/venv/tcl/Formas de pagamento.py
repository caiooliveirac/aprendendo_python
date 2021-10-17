pre = float(input("Qual o preço? "))
forma = input("Qual a forma de pagamento? ")
if "cartão" or "cartao" in forma.lower().split():
    parc = input("Deseja parcelar? ")
    if "sim" or "s" in parc.lower():
        numer = int(input("Deseja parcelar em quantas vezes? "))
        if numer == 2:
            print("Então vai pagar os {} reais em duas parcelas de {} reais.".format(round(pre),round(pre/2)))
        else:
            print("Nessas condições, terá um parcelamento de {}x de {} reais. Ao total, terá pago {} reais.".format(numer,round(pre*1.2/numer),round(pre*1.2)))
    else:
        print("Você vai pagar um valor de {} reais com o nosso desconto de 5%".format(round(pre*0.95)))
elif "cheque" or "dinheiro" or "a vista":
    print("Você vai pagar um valor de {} reais com o nosso desconto de 10%".format(round(pre*0.9)))
