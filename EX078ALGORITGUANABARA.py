lista = []
for c in range(0,15):
    num = int(input('Número: '))
    lista.append(num)
print(lista)
for p,v in enumerate(lista):
    if v % 10 == 0:
        print(f'Número {v} -> múltiplo de 10 encontrado na posição {p}')


