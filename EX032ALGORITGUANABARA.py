from random import randint
computador = randint(1,5)
usuario = int(input('TENTE ADIVINHAR O VALOR INTEIRO ESCOLHIDO PELO COMPUTADOR DE 1 A 5: '))
if usuario == computador:
    print('VOCÊ ADIVINHOU!')
else:
    print(f'VOCÊ ERROU! O NÚMERO ESCOLHIDO PELO COMPUTADOR FOI {computador}')