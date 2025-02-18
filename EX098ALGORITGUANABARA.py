def super_somador(n1,n2):
    acumulador =  0
    if n1 > n2:
        while True:
            if n2 > n1:
                break
            acumulador += n2
            n2 += 1
    else:
        while True:
            if n1 > n2:
                break
            acumulador += n1
            n1 += 1
    return acumulador

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print(f' A soma do intervalo fechado de {numero1} até {numero2} resultou em {super_somador(numero1,numero2)}')

