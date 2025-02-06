altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em KG: '))
if peso / altura ** 2 < 18.5:
    print('ABAIXO DO PESO')
elif  18.5 <= peso / altura ** 2 < 25:
    print('PESO IDEAL')
elif  25 <= peso / altura ** 2 < 30:
    print('SOBREPESO')
elif 30 <= peso / altura ** 2 <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')

