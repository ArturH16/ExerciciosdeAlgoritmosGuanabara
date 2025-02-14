mais_90 = menos_50_e_menos_160 = mais_100_e_mais190 = contador = acumulador_altura = 0
for  c in range(0,7):
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))
    if peso > 90:
        if peso > 100 and altura > 1.9:
            mais_100_e_mais190 += 1
        mais_90 += 1
    elif peso < 50 and altura < 1.6:
        menos_50_e_menos_160 += 1
    contador += 1
    acumulador_altura += altura
media_altura = acumulador_altura / contador
print(f'A média de altura é igual a {media_altura:.2f} m\nHá {mais_90} pessoas com mais de 90 kg\nHá {menos_50_e_menos_160} pessoas com menos de 50 kg e menos de 1.6 m\nHá {mais_100_e_mais190} pessoas com mais de 100 kg e mais de 1.9 m')


