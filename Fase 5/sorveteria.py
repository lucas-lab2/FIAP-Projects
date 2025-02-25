#Programa permite clientes escolherem a quantidade de sorvetes 
valor = 0
valor_cobertura = 0
valor_total = 0
#quantas bolas de sorvete
print("Bem-vindo à Sorveteria!")
print("Quantas opções de sorvete você deseja?")
print("1 Bola casquinha por R$ 6,00")
print("2 Bolas casquinha por R$ 9,00")
print("2 bolas cascão recheado por R$ 12,00")

opcao = int(input("Escolha: "))

match opcao:
    case 1:
        valo = 6
    case 2:
        valor = 9
    case 3:
        valor = 12
    case _:
        print("Opção inválida")
cobertura = input("Deseja cobertura? (S/N) ").lower()
if cobertura == "s":
    print("Escolha uma das opções de cobertura:")
    print("1 - Chocolate por R$ 2,00")
    print("2 - Morango por R$ 2,00")
    print("3 - Avelã por R$ 3,00")
    escolha = int(input())
    match escolha:
        case 1:
            valor_cobertura = 2
        case 2:
            valor_cobertura = 2
        case 3:
            valor_cobertura = 3
        case _:
            print("Opção inválida")
#quantidade de sorvetes
quantidade = int(input("Quantos sorvetes você deseja? "))
valor_total = (valor + valor_cobertura) * quantidade
print(f"O valor total é R$ {valor_total:.2f}")
    
#Se sim, oferece cobertura
