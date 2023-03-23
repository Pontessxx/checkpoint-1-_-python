def troca_sete(x):
    #Substitui todos os dígitos 7 por 0 em um número.
    resultado = 0 #inicia com 0
    multi = 1 #inicia com 1
    while x > 0:
        digito = x % 10
        if digito == 7:
            digito = 0       # qualquer 7 vira 0
        resultado += digito * multi #resultado
        multi = 10 * multi
        x //= 10 # x = x//10
    return resultado
while True:
    print("___________Team: Pontes____________")
    print("-    checkpoint 1 with python     -")
    print("___________________________________")
    print("\n*use numeros entre 0 a 99*")
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))

    if n1 < 0 or n1 > 99 or n2 < 0 or n2 > 99: #num pertencente 0 a 99
        print("\n Erro:")
        print("\n Os numeros devem estar entre 0 a 99")
        print("---Tente novamente!---")
    else:
        n1 = troca_sete(n1)
        n2 = troca_sete(n2)
        soma = n1 + n2
        soma = troca_sete(soma)
        if soma > 198: 
            print("erro: ultrapassou o limite de soma => 99 + 99 = 198")
            break

        print(f"Soma dos numeros: {soma}")
        break
#quantidade de vezes que tentei fazer : 7