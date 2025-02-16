from random import randint
lista = []
for c in range(0,30):
    computador = randint(1,15)
    lista.append(computador)
usuario = int(input('Digite um número de 1 a 15 e veja sua posição na lista e quantas vezes apareceu: '))
for p,v in enumerate(lista):
    if v == usuario:
        print(f'{usuario} encontrado na posição {p}')
print(f'Ele apareceu na lista um total de {lista.count(usuario)} vezes')