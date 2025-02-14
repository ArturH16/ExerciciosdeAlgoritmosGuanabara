from random import randint
maior_que_cinco = maior_que_tres = 0
for c in range(0,20):
    num = randint(0,10)
    if num > 5:
        maior_que_cinco  += 1
    if num % 3 == 0:
        maior_que_tres += 1
    print(f'Número sorteado: {num}')
print(f'Foram sorteados {maior_que_cinco} números maiores que 5\nForam sorteados {maior_que_tres} números maiores que 3')
