def maior(n1,n2):
    if n1 > n2:
        print(f'{n1} é maior que {n2}')
    elif n2 > n1:
        print(f'{n2} é maior que {n1}')
    else:
        print('Os dois números são iguais')


num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
maior(num1,num2)