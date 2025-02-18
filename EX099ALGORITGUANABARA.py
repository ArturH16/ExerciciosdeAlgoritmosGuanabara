def potencia(num,ex):
    return num ** ex

numero = float(input('Digite a base da potência: '))
expoente = float(input('Digite o expoente da base: '))
print(f'{numero} elevado a {expoente} resulta em {potencia(numero,expoente)}')