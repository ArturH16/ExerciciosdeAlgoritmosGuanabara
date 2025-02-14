num = acumulador =  0
while num != 1111:
    acumulador += num
    num = int(input('Digite um número inteiro: '))
print(f'O valor do somatório resultou em {acumulador}')