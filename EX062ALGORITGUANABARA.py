idade = acumulador = contador = maior_21 =  0
pergunta = 1
while pergunta != 0:
    idade = int(input('Idade: '))
    if idade > 21:
        maior_21 += 1
    acumulador += idade
    contador += 1
    pergunta = int(input('Quer continuar? Digite 0 para encerrar ou 1 para continuar: '))
    if pergunta == 0:
        pergunta = 0
media = acumulador / contador
print(f'{contador} idade(s) foram digitadas\nA média das idades é igual a {media:.2f} anos\n{maior_21} pessoa(s) tem mais de 21 anos')



