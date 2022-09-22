from random import randint
computador = randint(0,10)
print("Ola, eu sou seu computador")
print("Escolhi um numero de 1 a 10")
print("Tente advinhar qual escolhi")
n = int(input("Digite o numero: "))
palpite = 0
while n != computador:
    palpite = palpite + 1
    n = int(input("Errou! tente novamente: "))
print("Parabens, voce venceu!, usando o total de {} palpites!".format(palpite))