lista = []
for c in range(0,10):
    num = int(input('Número: '))
    lista.append(num)
print(lista)
for p,v in enumerate(lista):
    if v % 2 == 0:
        print(f'Número {v} -> número par encontrado na posição {p}')