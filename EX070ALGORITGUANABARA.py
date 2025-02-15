c = num2 = 0
a = num = ultimo = penultimo = 1
count = 0
while count <= 1:
    print(num)
    count += 1
count = 2
while  2 <= count < 10:
    num = ultimo + penultimo
    print(num)
    penultimo = ultimo
    ultimo = num
    count += 1


