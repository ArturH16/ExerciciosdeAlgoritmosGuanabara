from random import choice
jokenpo_usuario = str(input('Digite PEDRA, PAPEL ou TESOURA: ')).upper()
jokenpo_maquina = ['PEDRA','PAPEL','TESOURA']
escolha_maquina = choice(jokenpo_maquina)
print(f'A MÁQUINA ESCOLHEU {escolha_maquina}')
if jokenpo_usuario == escolha_maquina:
    print('EMPATE')
elif jokenpo_usuario == 'PEDRA' and escolha_maquina == 'PAPEL' or jokenpo_usuario == 'PAPEL' and escolha_maquina == 'TESOURA' or jokenpo_usuario == 'TESOURA' and escolha_maquina == 'PEDRA':
    print('A MÁQUINA VENCEU')
else:
    print('VOCÊ VENCEU!')

