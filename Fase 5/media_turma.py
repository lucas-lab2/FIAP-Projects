alunos_total = int(input("Digite o número total de alunos:"))
soma_notas = 0
for i in range(alunos_total):
    notas = float(input(f"Digite a nota do aluno {i +1}:"))
    soma_notas += notas
media = soma_notas / alunos_total
print("A média da turma é:", media)
