num1 = input("Me diga um número: ")
num2 = input("Me diga um número: ")
num3 = input("Me diga um número: ")

if num3 >= num2:
    if num3 >= num1:
        print(num3,"é o maior")
elif num2 >= num1:
    if num2 >= num3:
        print(num2,"é o maior")
    elif num1 >= num2:
        if num1 >= num3:
            print(num1,"é o maior")


if num3 <= num2:
    if num3 <= num1:
        print(num3,"é o menor")
elif num2 <= num1:
    if num2 <= num3:
        print(num2,"é o menor")
    elif num1 <= num2:
        if num1 <= num3:
            print(num1,"é o menor")


