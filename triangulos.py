r1 = float(input("Primeiro segmento"))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM formar o triangulo!")
    if r1 == r2 == r3:
        print("EQUILATERO!")
    elif r1 != r2 and r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISOCELES!")

else:
    print("Os segmentos a cima nao podem formal um triangulo ")