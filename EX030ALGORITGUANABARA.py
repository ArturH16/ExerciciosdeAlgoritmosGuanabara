segmento_um = float(input('Digite o valor do primeiro segmento de reta: '))
segmento_dois = float(input('Digite o valor do segundo segmento de reta: '))
segmento_tres = float(input('Digite o valor do terceiro segmento de reta: '))
if segmento_um + segmento_dois > segmento_tres and segmento_um + segmento_tres > segmento_dois and segmento_dois + segmento_tres > segmento_um:
    print('É possível formar um triângulo')
    if segmento_um == segmento_dois == segmento_tres:
        print('TRIÂNGULO EQUILÁTERO')
    elif segmento_um != segmento_dois and segmento_um != segmento_tres and segmento_dois != segmento_tres:
        print('TRIÂNGULO ESCALENO')
    else:
        print('TRIÂNGULO ISÓSCELES')
else:
    print('Não é possível formar um triângulo')
