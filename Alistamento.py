n1 = float(input("DIGITE A PRIMEIRA NOTA: "))
n2= float(input("DIGITE A SEGUNDA NOTA: "))
media = (n1 + n2)/ 2
print("Tirando {:.1f} e {:.1f}, a media do aluno e de {}".format(n1,n2,media))

if media >= 5 and media < 7:
    print("Recuperacao")
elif media > 7.0:
    print("Aprovado")
else:
    print("Reprovado")
