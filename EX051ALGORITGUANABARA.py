maior = menor = 0
for c in range(0,8):
    produto = float(input('Diigte o preço do produto: '))
    if c == 0:
        maior = menor = produto
    else:
        if produto > maior:
            maior = produto
        elif produto < menor:
            menor = produto
print(f'O maior preço digitado foi R${maior:.2f} e o menor foi R${menor:.2f}')