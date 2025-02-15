c = mulheres = homens_pesados = peso_mulheres = maior_peso_homem  =  0
while True:
    genero_biologico = input('Digite o gênero biológico [M ou F]: ')
    peso = float(input('Digite o peso: '))
    if genero_biologico.upper() == 'F':
        mulheres += 1
        peso_mulheres += peso
    if genero_biologico.upper() == 'M':
        if c == 0:
            maior_peso_homem = peso
        else:
            if peso > maior_peso_homem:
                maior_peso_homem = peso
        if peso > 100:
            homens_pesados += 1
    c += 1
    if c == 8:
        break
media_mulheres = peso_mulheres / mulheres
print(f'{mulheres} mulheres foram cadastradas\n{homens_pesados} homens pesam mais de 100 kg\nA média de peso entre as mulheres é de {media_mulheres:.2f} kg\n{maior_peso_homem} kg foi o maior peso registrado entre os homens')

