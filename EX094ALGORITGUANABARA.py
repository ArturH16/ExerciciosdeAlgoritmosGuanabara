def fibonnaci(termos):
    num = ultimo = penultimo = 1
    count = 0
    while count <= 1:
        if termos == 1:
            print(f'{num} >> ',end='')
            break
        else:
            print(f'{num} >> ',end='')
        count += 1
    count = 2
    while  2 <= count < termos:
        num = ultimo + penultimo
        print(f'{num} >> ',end='')
        penultimo = ultimo
        ultimo = num
        count += 1
    print('FIM')


termos_fibonnaci = int(input('Quantos termos da sequência de Fibonnaci você quer ver: '))
fibonnaci(termos_fibonnaci)

