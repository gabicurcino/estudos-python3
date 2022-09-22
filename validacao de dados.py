s = str(input("Qual o sexo da pessoa? [M/F]:")).strip().upper() [0]
while s not in "MmFf" :
    s = str(input("Dados invalidos digite novamente: "))
print("Dados validados com sucesso")
