c = 1
par = impar = 0
while c <= 6:
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    c += 1
print(f'Ao todo, foram digitados {par} números pares e {impar} números impares')