print("******************************")
print("***checkpoint 1 with python***")
print("******************************")

print("use numeros entre 0 a 99")

while True:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))

    if n1 < 0 or n1 > 99 or n2 < 0 or n2 > 99:
        print("\n Erro:")
        print("\n Os numeros devem estar entre 0 a 99")
        print("---Tente novamente!---")
    else:
        #subistituir numeros 7 em 0
        n1 = int(str(n1).replace('7', '0'))
        n2 = int(str(n2).replace('7', '0'))

        soma_teste = n1 + n2
        if '7' in str(soma_teste):
            soma_teste = int(str(soma_teste).replace('7','0'))

        print(f"Soma dos numeros: {n1} + {n2} = {soma_teste}")
        break

#teste numero 2 
# não devo usar string tentar novaemnte
