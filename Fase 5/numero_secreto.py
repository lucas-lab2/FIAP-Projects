import random

numero_secreto = random.randint(1, 100)
tentativas = 0
advinhou = False

while not advinhou:
    tentativa = int(input("Digite um número: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print("Parabéns, você acertou!")
        print(f"Você tentou {tentativas} vezes")
        advinhou = True
    elif tentativa < numero_secreto:
        print("Digite um número maior")
    else:
        print("Digite um número menor")
