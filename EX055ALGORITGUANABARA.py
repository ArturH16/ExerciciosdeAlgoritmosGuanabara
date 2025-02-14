from random import randint
condicao = True
computador = randint(1,10)
contador = 0
print('JOGO DA ADIVINHAÇÃO -> 4 CHANCES')
while condicao:
    usuario = int(input('TENTE ADIVINHAR O VALOR INTEIRO ESCOLHIDO PELO COMPUTADOR DE 1 A 10 : '))
    contador += 1
    if usuario == computador:
        print('VOCÊ ADIVINHOU!')
        condicao = False
    else:
        if contador == 4:
            print(f'VOCÊ ERROU NOVAMENTE E SUAS CHANCES SE ESGOTARAM! O VALOR ESCOLHIDO PELO COMPUTADOR ERA {computador}')
            condicao = False
        else:
            print('VOCÊ ERROU! TENTE NOVAMENTE')
