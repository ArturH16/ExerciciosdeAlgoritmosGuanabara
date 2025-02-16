nomes = []
generos_biologicos = []
salarios = []
for c in range(0,5):
    nome = input('Nome: ')
    nomes.append(nome)
    genero_biologico = input('Gênero Biológico[M ou F]: ')
    generos_biologicos.append(genero_biologico)
    salario = float(input('Salário: '))
    salarios.append(salario)
print('DADOS DAS FUNCIONÁRIAS MULHERES')
for pos,n in enumerate(nomes):
    for g,mf in enumerate(generos_biologicos):
        if mf.upper() == 'F':
            for p,s in enumerate(salarios):
                if g == p and g == p and g == pos:
                    print(f'Pessoa: {n}\nGênero Biológico: {mf}\nSalário: R${s:.2f}')