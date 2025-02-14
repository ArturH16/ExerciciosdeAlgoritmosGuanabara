mulheres = homens = maior_que_vinte_mulheres = idade_acumulador =  idade_homens =  0
for c in range(0,5):
    idade = int(input('Idade: '))
    pessoa = input('Sexo Biológico[M ou F]: ')
    if pessoa.upper() == 'F':
        if idade > 20:
            maior_que_vinte_mulheres += 1
        mulheres += 1
    elif pessoa.upper() == 'M':
        homens += 1
        idade_homens += idade
    idade_acumulador += idade
media_grupo = idade_acumulador /(homens + mulheres)
media_homens = idade_homens / homens
print(f'A média de idade do grupo foi de {media_grupo:.2f} anos\nForam cadastrados {homens} homens\nForam cadastradas {mulheres} mulheres\nA média de idade dos homens é de {media_homens:.2f} anos\nForam cadastradas {maior_que_vinte_mulheres} mulheres com mais de 20 anos')