from time import sleep
inicio = int(input('Digite um número inteiro onde vai começar a contagem: '))
final = int(input('Digite um número inteiro onde vai terminar a contagem: '))
incremento = int(input('Digite o valor do incremento: '))
while True:
    if final < inicio:
        incremento = abs(incremento)
        print(f'{inicio} ',end='')
        inicio -= incremento
        if inicio < final:
            break
    else:
        print(f'{inicio} ', end='')
        inicio += incremento
        if inicio > final:
            break
    sleep(1)
print('\nAcabou!')