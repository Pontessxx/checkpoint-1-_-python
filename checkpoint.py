def replace_sevens(n):
    """Substitui todos os dígitos 7 por 0 em um número."""
    result = 0
    multiplier = 1
    while n > 0:
        digit = n % 10
        if digit == 7:
            digit = 0
        result += digit * multiplier
        multiplier *= 10
        n //= 10
    return result
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

        n1 = replace_sevens
        

        print(f"Soma dos numeros: {n1} + {n2} = {soma_teste}")
        break
    
# não devo usar string tentar novaemnte
