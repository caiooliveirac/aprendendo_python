not1 = float(input("Nota no primeiro bimestre: "))
not2 = float(input("Nota no segundo bimestre: "))
not3 = float(input("Nota no terceiro bimestre: "))
not4 = float(input("Nota no quarto bimestre: "))

media = (not1 + not2 + not3 + not4)/4

if media >= 7:
    print("Aprovado direto com média",round(media,1))
elif media >= 5:
    print("Ficou na recuperação com média",round(media,1))
else:
    print("Perdeu de ano")