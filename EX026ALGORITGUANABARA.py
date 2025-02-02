maior =  menor =  0
for c in range(0,2):
    num = int(input('Digite um número inteiro: '))
    if c == 0:
        maior =  menor = num
    else:
        if num > maior:
            maior = num
        elif menor == maior:
            menor = num
if menor == maior:
    print('Não há valor maior, os dois são iguais')
else:
    print(f'O maior valor digitado foi {maior}')
