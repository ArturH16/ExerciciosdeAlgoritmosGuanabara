def Gerador(m,l):
    print('-'*l)
    print(m)
    print('-'*l)


mensagem = input('Digite uma mensagem: ')
linhas = int(input('Digite a quantidade de linhas que terá antes e depois da exibição da mensagem: '))
Gerador(mensagem,linhas)