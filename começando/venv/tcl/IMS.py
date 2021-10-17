peso = float(input("Me diga o seu peso: "))
altura = float(input("Me diga sua altura: "))

imc = peso/(altura**2)

if round(imc) > 40:
    print("Obeso mórbido")
elif round(imc) > 30:
    print("Obeso")
elif round(imc) > 25:
    print("Sobrepeso")
elif round(imc) > 18.5:
    print("Peso ideal")
else:
    print("Abaixo do peso")