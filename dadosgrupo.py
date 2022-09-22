h = 0
m = 0
contidade = 0
while True:
    idade = int(input("Digite a idade: "))
    if idade > 18:
        contidade += 1
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
        if sexo == 'M':
            h += 1
        if sexo == 'F':
            if idade > 20:
                m += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print(f"A quantidade de pessoas com mais de 18 e de {contidade} e a quantidade de homens e de {h}")
print(f"A quantidade de mulheres com mais de 20 anos e de {m}")







