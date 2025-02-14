
condicao = True
nome_mulher_mais_jovem = ''
nome_pessoa_mais_velha  = ''
homens = contador = homens_mais_de_30 = mulheres_menos_18 = maior = mulheres = menor_idade_mulher = acumulador =  0
while condicao:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    genero_biologico = input('Gênero Biológico[M ou F]: ')
    contador += 1
    acumulador += idade
    pergunta = input('Quer continuar[S ou N]: ')
    if pergunta.upper() == 'N':
        condicao = False
    if contador == 1:
        maior = idade
        nome_pessoa_mais_velha = nome
    else:
        if idade > maior:
            maior = idade
            nome_pessoa_mais_velha = nome
    if genero_biologico.upper() == 'F':
        mulheres += 1
        if mulheres == 1:
            nome_mulher_mais_jovem = nome
            menor_idade_mulher = idade
        else:
            if idade < menor_idade_mulher:
                menor_idade_mulher = idade
                nome_mulher_mais_jovem = nome
        if idade < 18:
            mulheres_menos_18 += 1
    if genero_biologico.upper() == 'M':
        if idade > 30:
            homens_mais_de_30 += 1
media = acumulador / contador
print(f'O nome da pessoa mais velha é {nome_pessoa_mais_velha}\nO nome da mulher mais jovem é {nome_mulher_mais_jovem}\nA média de idade do grupo é igual a {media:.2f}\n{homens_mais_de_30} homens tem mais de 30 anos\n{mulheres_menos_18} mulheres tem menos de 18 anos')
