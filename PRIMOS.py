num = int(input("Digite um numero: "))
tot = 0
for c in range(1, num + 1):
    if num % c ==0:
        print("\033[33m")
        tot += 1
    else:
        print("\033[31m")
    print("{}".format(c), end= " ")
print("\n\033[mO numero {} foi divisivel {} vezes".format(num,tot))
if tot == 2:
    print("E por isso ele e PRIMO")
else:
    print("E por isso ele NAO e primo")
