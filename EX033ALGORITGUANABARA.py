valor_casa = float(input('Digite o valor da casa em R$: '))
tempo = int(input('Você pretende pagar a casa em quantos anos: '))
salario = float(input('Digite seu salário em R$: '))
if valor_casa / (tempo * 12) > salario * 0.3:
    print('EMPRÉSTIMO NEGADO')
else:
    print('EMPRÉSTIMO APROVADO')