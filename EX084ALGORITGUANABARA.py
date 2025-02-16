nomes = []
idades = []
for c in range(0,9):
    nome = input('Nome: ')
    nomes.append(nome)
    idade = int(input('Idade: '))
    idades.append(idade)
for c,n in enumerate(nomes):
    for p,i in enumerate(idades):
        if i < 18 and c == p:
            print(f'Pessoa: {n}\nIdade: {i}')