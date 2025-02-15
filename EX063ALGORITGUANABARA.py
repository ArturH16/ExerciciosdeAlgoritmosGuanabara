a = acumulador = contador = par =  menor = 0
while a == 0:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par += 1
    if contador == 0:
        menor = num
    else:
        if num < menor:
            menor = num
    acumulador += num
    contador += 1
    a = int(input('Quer continuar?[Digite 0 para continuar e qualquer outro número inteiro para continuar]: '))
media = acumulador / contador
print(f'O somatório resultou em {acumulador}\nO menor valor digitado foi {menor}\nA média dos valores digitados é igual a {media:.2f}\n{par} valores são pares')
