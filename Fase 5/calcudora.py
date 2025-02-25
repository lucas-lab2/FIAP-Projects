print("Bem vindo a calculadora")
print("Digite qual operaçao deseja fazer")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = int(input("Escolha: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match escolha:
    case 1:
        print(f"A soma é {num1 + num2}")
    case 2:
        print(f"A subtração é {num1 - num2}")
    case 3:
        print(f"A multiplicação é {num1 * num2}")
    case 4:
        print(f"A divisão é {num1 / num2}")
    case _: #utilizado em caso o usuário digiete uma opção inválida
        print("Opção inválida")

