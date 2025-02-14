condicao =  True
maior_idade = homens = mulheres = idade_homens = mulher_mais_jovem = contador = maior = 0
while condicao:
    idade = int(input('Idade: '))
    genero_biologico = input('Gênero Biológico[M ou F]: ')
    contador += 1
    pergunta = input('Quer continuar[S OU N]: ')
    if pergunta.upper() == 'N':
        condicao = False
    if contador == 1:
        maior = idade
    else:
        if idade > maior:
            maior = idade
    if genero_biologico.upper() == 'M':
        homens += 1
        idade_homens += idade
    if genero_biologico.upper() == 'F':
        mulheres += 1
        if mulheres == 1:
            mulher_mais_jovem = idade
        else:
            if idade < mulher_mais_jovem:
                mulher_mais_jovem = idade
media_homens = idade_homens / homens
print(f'A maior idade lida foi {maior}\n{homens} homens foram cadastrados\nA idade da mulher mais jovem é igual a {mulher_mais_jovem}\nA média de idade dos homens é igual a {media_homens:.2f}')
