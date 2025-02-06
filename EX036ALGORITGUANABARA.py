horas_atividades_fisicas = int(input('Quantas horas mensais você pratica de exercícios físicos: '))
pontos = 0
if horas_atividades_fisicas <= 10:
    pontos += 2
elif  10 < horas_atividades_fisicas <= 20:
    pontos += 5
else:
    pontos += 10
print(f'Você conseguiu 10 pontos, que convertendo para reais, é igual a R${pontos * 0.05}')