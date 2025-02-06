nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário atual do empregado: R$'))
tempo = int(input('Quanto anos ele trabalha na empresa: '))
if tempo < 3:
    reajuste = salario * 1.03
    print(f'O salário sofreu um reajuste de 3%, e o novo valor é de R${reajuste:.2f}')
elif 3 < tempo < 10:
    reajuste = salario *1.125
    print(f'O salário sofreu um reajuste de 12,5%, e o novo valor é de R${reajuste:.2f}')
else:
    reajuste = salario * 1.2
    print(f'O salário sofreu um reajuste de 20%, e o novo valor é de R${reajuste:.2f}')