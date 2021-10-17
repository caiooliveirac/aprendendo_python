ida = int(input("Quantos anos você completa até dezembro deste ano? "))

if ida == 18:
    print("Este é o ano de você se alistar")
elif ida > 18:
    print("Já passou da hora de você se alistar. Pague a multa de {} reais na casa lotérica e se aliste".format(float(round((ida-18)*0.17,2))))
else:
    print("Ainda não é sua hora de se alistar")