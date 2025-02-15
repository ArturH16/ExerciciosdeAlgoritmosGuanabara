c = 0
num = int(input('Digite um número para descobrir sua tabuada: '))
while True:
    c += 1
    if c > 10:
        break
    print(f'5 x {c} = {5 * c}')