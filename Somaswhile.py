n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print('''    [ 1 ]somar
    [ 2 ]multiplicar
    [ 3 ]maior
    [ 4 ]novos numeros
    [ 5 ]sair do programa''')
    opcao = int(input("Qual e sua opcao? "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} e {} e de {}".format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print("A multiplicacao de {} x {} e de {}".format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("entre {} e {} o maior valor e de {}".format(n1,n2,maior))
    elif opcao == 4:
        print("Informe os numeros novamente")
        n1= int(input("Digite o primeiro valor"))
        n2= int(input("Digite o segundo valor"))
    elif opcao ==5:
        print("Finalizando...")

    else:
        print("opcao invalida,tente novamente")
    print('=-=' * 10)

print("Fim do programa, volte sempre!")


