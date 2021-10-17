ret1 = int(input("Reta1: "))
ret2 = int(input("Reta2: "))
ret3 = int(input("Reta3: "))

if ret3 < ret2 + ret1:
    if ret2 < ret3 + ret1:
        if ret1 < ret3 + ret2:
            print("Sim! Dá para formar um triângulo com essas retas!")
            if ret1 == ret2 == ret3:
                print("Este triângulo será equilátero")
            elif ret1 == ret2 or ret1 == ret3 or ret2 == ret3:
                print("Este triângulo será isósceles")
            else:
                print("Este triângulo será escaleno")
        else:
            print("Isso aí não forma um triângulo.")
    else:
        print("Isso aí não forma um triângulo.")
else:
    print("Isso aí não forma um triângulo.")

print("Sim! Dá para formar um triângulo com essas retas!" if ret3 < ret2 + ret1 and ret2 < ret1 + ret3 and ret1 < ret2 + ret3 else "Isso aí não forma um triângulo")