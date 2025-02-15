num = int(input('Digite o número onde vai começar a PA: '))
razao = int(input('Digite a razão da PA: '))
c = acumulador = 0
while True:
    if c == 10:
        break
    else:
        acumulador += num
        print(num,end=' ')
        num += razao
        c += 1
print(f'\nA soma dos 10 primeiros valores dessa PA resultaram em {acumulador}')
