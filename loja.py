print("{:=^40}".format("LOJAS XYZ"))
preco = float(input("Preco das compras: R$: "))
print('''FORMAS DE PAGAMENTO
[ 1 ] A vista dinheiro/ cheque
[ 2 ] A vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input("Qual a forma de pagamento?"))
if opcao == 1:
    total = preco - (preco *10 / 100)
elif opcao == 2:
    total = preco - (preco *5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra sera parcelada em 2x de {:.2f}".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input("Quantas parceals? "))
    parcela = total / totalparc
    print("Sua compra sera parcelada em {}x vezes de {:.2f} COM JUROS".format(totalparc, parcela))
else:
    total = 0
    print("Opcao de pagamento invalida, tente novamente!")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total))


