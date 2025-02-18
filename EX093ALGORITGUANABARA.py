def contador(i,f,inc):
    while True:
        print(f'{i} >>',end=' ')
        i += inc
        if i >= f:
            print('FIM')
            break



inicio = int(input('Digite onde começa a contagem: '))
fim = int(input('Digite o fim da contagem: '))
incremento = int(input('Digite o incremento: '))
contador(inicio,fim,incremento)