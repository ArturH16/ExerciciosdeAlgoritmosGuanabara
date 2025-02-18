def media(n1,n2):
    media_aluno = (n1 + n2) / 2
    return media_aluno


def situacao(sit):
    if sit >= 7:
        return 'APROVADO'
    elif 6 <= sit < 7:
        return 'RECUPERAÇÃO'
    else:
        return 'REPROVADO'
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print(f'A média do aluno é igual a {media(nota1,nota2)}')
print(f'SITUAÇÃO DO ALUNO = {situacao(media(nota1,nota2))}')