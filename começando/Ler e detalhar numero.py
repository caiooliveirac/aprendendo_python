num = input("Digite um numero até 9999:")
print ('unidade:',num[len(num)-1])
if int(num) > 9:
    print ('dezena:',num[len(num)-2])
if int(num) > 99:
    print ('centena:',num[len(num)-3])
if int(num) > 999:
    print ('milhar:',num[len(num)-4])