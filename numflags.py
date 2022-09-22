n = int(input("Digite um numero(999 para parar): "))
soma = 0
cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um numero: "))
    if n == 999:
        break
print(f"Voce digitou {cont} numeros e a soma entre eles e igual a {soma}")
