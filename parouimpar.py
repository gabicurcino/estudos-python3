from random import randint
v = 0
while True:
   p = int(input("Digite um valor "))
   c = randint(0,11)
   total = p + c
   tipo = " "
   while tipo not in 'PI':
       tipo = str(input("Par ou impar? [P/I] ")).strip().upper()[0]
   print(f"Voce jogou {p} e o computador {c}. Total de {total}", end = "")
   print("DEU PAR" if total % 2 == 0 else "Deu impar")
   if tipo == 'P':
       if total % 2 == 0:
           print("Voce venceu!")
           v += 1
       else:
           print("Voce perdeu")
           break
   elif tipo == 'I':
       if total % 2 == 1:
           print("Voce venceu!")
           v += 1
       else:
           print("Voce perdeu")
           break
print("Vamos jogar novamente!")

