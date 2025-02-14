condicao = True
salario_mulher = salario_homem = homem = mulher = 0
while condicao:
    salario = float(input('Salário: '))
    genero_biologico = input('Sexo Biológico[M OU F]: ')
    if genero_biologico.upper() == 'M':
        salario_homem += salario
        homem += 1
    elif genero_biologico.upper() == 'F':
        salario_mulher += salario
        mulher += 1
    pergunta = input('Quer continuar?[S OU N]: ')
    if pergunta.upper() == 'N':
        condicao = False
print(f'O total de salários dos homens foi de R${salario_homem:.2f}\nO toal de salários das mulheres foi de R${salario_mulher:.2f}')
