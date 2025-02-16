lista = []
acumulador_nota = contador_nota = maior_nota = 0
for c in range(0,10):
    nota = int(input('Nota: '))
    acumulador_nota += nota
    contador_nota += 1
    lista.append(nota)
    if c == 0:
        maior_nota = nota
    else:
        if nota > maior_nota:
            maior_nota = nota
media = acumulador_nota / contador_nota
alunos_acima_media = 0
print(f'A média da turma é igual a {media:.2f}\nA maior nota foi {maior_nota}')
for p,n in enumerate(lista):
    if n > media:
        alunos_acima_media += 1
    if n == maior_nota:
        print(f'A maior nota aparece na posição {p}')
print(f'Na turma, {alunos_acima_media} aluno(s) ficaram acima da média')