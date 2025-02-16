c = num2 = 0
a = num = ultimo = penultimo = 1
lista = []
count = 0
while count <= 1:
    lista.append(num)
    count += 1
count = 2
while  2 <= count <= 15:
    num = ultimo + penultimo
    lista.append(num)
    penultimo = ultimo
    ultimo = num
    count += 1
print(lista)