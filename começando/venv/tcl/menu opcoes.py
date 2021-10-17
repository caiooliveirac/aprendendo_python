val1 = int(input("Me dê um valor: "))
val2 = int(input("Me dê outro valor: "))

fazer = int(input("O que deseja fazer com eles? \n [1] somar \n [2] multiplicar \n [3] dizer o maior \n [4] pedir novos números \n [5] sair do programa \n"))

while fazer != 5:
    if fazer == 1:
        print(val1 + val2)
        fazer = int(input(
            "O que deseja fazer com eles? \n [1] somar \n [2] multiplicar \n [3] dizer o maior \n [4] pedir novos números \n [5] sair do programa \n"))

    elif fazer == 2:
        print (val1 * val2)
        fazer = int(input(
            "O que deseja fazer com eles? \n [1] somar \n [2] multiplicar \n [3] dizer o maior \n [4] pedir novos números \n [5] sair do programa \n"))

    elif fazer == 3:
        if val1 > val2:
            print("{} é o maior".format(val1))
        else:
            print("{} é o maior".format(val2))
        fazer = int(input(
            "O que deseja fazer com eles? \n [1] somar \n [2] multiplicar \n [3] dizer o maior \n [4] pedir novos números \n [5] sair do programa \n"))

    elif fazer == 4:
        val1 = int(input("Me dê um valor: "))
        val2 = int(input("Me dê outro valor: "))
        fazer = int(input(
            "O que deseja fazer com eles? \n [1] somar \n [2] multiplicar \n [3] dizer o maior \n [4] pedir novos números \n [5] sair do programa \n"))

print("Bom dia! Obrigado por utilizar nosso serviço")