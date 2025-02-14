maior_de_dezoito = menor_de_cinco = maior = acumulador_idade = contador = 0
for c in range(0,10):
    idade = int(input('Digite a idade: '))
    if c == 0:
        maior = idade
    else:
        if idade > maior:
            maior = idade
    if idade > 18:
        maior_de_dezoito += 1
    elif idade < 5:
        menor_de_cinco += 1
    acumulador_idade += idade
    contador += 1
media = acumulador_idade / contador
print(f'A média de idade do grupo é de {media:.2f} anos\n{maior_de_dezoito} pessoas tem mais de 18 anos\n{menor_de_cinco} pessoas tem menos de 5 anos')
