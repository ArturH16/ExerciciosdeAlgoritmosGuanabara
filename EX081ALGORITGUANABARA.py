lista = []
acumulador_idade = contador_idade = maior = 0
for c in range(0,8):
    idade = int(input('Idade: '))
    acumulador_idade += idade
    contador_idade += 1
    lista.append(idade)
    if c == 0:
        maior = idade
    else:
        if idade > maior:
            maior = idade
media = acumulador_idade / contador_idade
print(f'A média de idade do grupo é igual a {media:.2f}')
print(f'A maior idade do grupo foi {maior} anos')
for p,v in enumerate(lista):
    if v > 25:
        print(f'Na posição {p}, temos idade maior que 25 anos: {v} anos')
    if v == maior:
        print(f'Na posição {p}, foi registrada a maior idade: {maior} anos')

