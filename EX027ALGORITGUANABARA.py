quantidade_de_notas = total_de_notas = 0
for c in range(0,2):
    nota = float(input('Digite a nota do aluno: '))
    total_de_notas += nota
    quantidade_de_notas += 1
media = total_de_notas / quantidade_de_notas
if media <= 4.9:
    print(f'O aluno foi reprovado pela média de {media:.2f}')
elif 5 <= media <= 6.9:
    print(f'O aluno vai para a recuperação pela média de {media:.2f}')
else:
    print(f'O aluno foi aprovado pela média de {media:.2f}')
