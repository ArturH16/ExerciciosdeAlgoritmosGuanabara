def Gerador(m,r,b):
    borda1, borda2, borda3 = '+-------=======------+', '~~~~~~~~:::::::~~~~~~~', '<<<<<<<<------->>>>>>>'
    if b == 1:
        for c in range(r):
            print(borda1)
            print(m)
            print(borda1)
            print('-='*30)
    elif b == 2:
        for c in range(r):
            print(borda2)
            print(m)
            print(borda2)
            print('-='*30)

    elif b == 3:
        for c in range(r):
            print(borda3)
            print(m)
            print(borda3)
            print('-='*30)


mensagem = input('Digite uma mensagem: ')
print(f'OPÇÕES DE BORDAS PARA A MENSAGEM\nBORDA1: +-------=======------+\nBORDA2: ~~~~~~~~:::::::~~~~~~~\nBORDA3: <<<<<<<<------->>>>>>>')
escolha_borda = int(input('Qual borda você escolhe? [Digite 1 para borda 1, 2 para a borda 2 e 3 para a borda 3]: '))
repeticao = int(input('Quantas vezes você quer que apareça essa mensagem na tela: '))
Gerador(mensagem,repeticao,escolha_borda)
