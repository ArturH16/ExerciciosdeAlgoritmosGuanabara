tipo_carro = str(input('CARRO POPULAR OU DE LUXO[USE P OU L]: '))
dias = int(input('Quantos dias de aluguel: '))
km = float(input('Quantos km percorridos: '))
if tipo_carro.upper() == 'P':
    if km <= 100:
        formula = 90 * dias + 0.2 * km
        print(f'O valor a ser pago pelo aluguel é de R${formula:.2f}')
    else:
        formula = 90 * dias + 0.1 * km
        print(f'O valor a ser pago pelo aluguel é de R${formula:.2f}')
elif tipo_carro.upper() == 'L':
    if km <= 200:
        formula = 150 * dias + 0.3 * km
        print(f'O valor a ser pago pelo aluguel é de R${formula:.2f}')
    else:
        formula = 150 * dias + 0.25 * km
        print(f'O valor a ser pago pelo aluguel é de R${formula:.2f}')


