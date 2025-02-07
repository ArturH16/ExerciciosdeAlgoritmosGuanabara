from time import sleep
usuario = int(input('Digite um número inteiro positivo: '))
print(' CONTAGEM ')
c = 0
while c <= usuario:
    print(c)
    sleep(1)
    c += 1
print('Acabou')