def Gerador(m,l):
    print('-'*l)
    print(m)
    print('-'*l)

def repeticoes(r):
    for c in range(r):
        print('-='*30)
        Gerador(mensagem,linhas)


mensagem = input('Digite uma mensagem: ')
linhas = int(input('Digite a quantidade de linhas que terá antes e depois da exibição da mensagem: '))
repeticao = int(input('Você quer que apareça essa mensagem quantas vezes na tela: '))
repeticoes(repeticao)