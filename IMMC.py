peso = float(input("Qual e seu peso KG? "))
altura = float(input("Qual sua altura? "))
imc = peso / (altura **2)
print("O IMC dessa pessoa e de {:.1f}".format(imc))
if imc < 18.5:
    print("Voce esta abaixo do peso normal")
elif 18.5 <= imc < 25:
    print("Parabens voce esta na faixa de peso normal")
elif 25 <= imc < 30:
    print("Voce esta a cima do peso")
elif 30 <= imc < 40:
    print("Voce esta em obesidade, cuidado!")
elif imc >= 40:
    print("Voce esta em obesidade morbida, cuidado!")
