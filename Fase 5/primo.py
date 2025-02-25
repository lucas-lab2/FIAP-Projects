#Este programa verifica se o número é primo ou não

numero = int(input("Digite um número maior que 1: "))

if numero <= 1:
    print("Digite um número válido")
else:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(f"O número {numero} é primo")
    else:
        print(f"O número {numero} não é primo")