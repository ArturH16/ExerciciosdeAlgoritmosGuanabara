condicao = True
alunos = acumulador =  0
while condicao:
    idade_aluno = int(input('Idade do Aluno: '))
    if idade_aluno == 999:
        condicao = False
    else:
        alunos += 1
        acumulador += idade_aluno
if alunos != 0:
    media = acumulador / alunos
    print(f'A média de idade dos alunos é igual a {media:.2f}')

