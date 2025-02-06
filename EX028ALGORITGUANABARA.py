largura = float(input('Digite a largura do terreno em m²: '))
comprimento = float(input('Digite o comprimento do terreno em m²: '))
area = largura * comprimento
if area < 100:
    print(f'TERRENO POPULAR COM {area:.2f} m²')
elif 100 <= area <= 500:
    print(f'TERRENO MASTER COM {area:.2f} m²')
else:
    print(f'TERRENO VIP COM {area:.2f} m²')