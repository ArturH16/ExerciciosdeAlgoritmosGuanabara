from random import randint
lista = []
for c in range(0,20):
    computador = randint(0,99)
    lista.append(computador)
lista.sort()
print(lista)
