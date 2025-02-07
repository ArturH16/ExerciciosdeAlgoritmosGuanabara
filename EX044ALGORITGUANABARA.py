from time import sleep
inicio = int(input('Digite um número inteiro onde vai começar a contagem: '))
final = int(input('Digite um número inteiro onde vai terminar a contagem: '))
incremento = int(input('Digite o valor do incremento: '))
while final >= inicio:
    print(f'{inicio} ',end='')
    sleep(1)
    inicio += incremento
print('\nAcabou!')