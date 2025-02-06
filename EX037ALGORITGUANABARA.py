genero_biologico = str(input('Digite seu gênero biológico[M/F]: '))
salario = float(input('Qual o salário atual: '))
tempo = int(input('Quanto tempo na empresa: '))
reajuste = 0
if genero_biologico.upper() == 'F':
    if tempo < 15:
        reajuste = salario * 1.05
    elif 15 <= tempo <= 20:
        reajuste = salario * 1.12
    else:
        reajuste = salario * 1.23
if genero_biologico.upper() == 'M':
    if tempo < 20:
        reajuste = salario * 1.03
    elif 20 <= tempo <= 30:
        reajuste = salario * 1.13
    else:
        reajuste = salario * 1.25
print(f'O novo salário é de R${reajuste:.2f}')