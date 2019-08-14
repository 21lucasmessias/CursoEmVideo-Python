from random import randint
vit = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    print('=-' * 20)
    player = int(input('Digite um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print('-' *40)
    pc = randint(1, 20)
    resto = (player + pc) % 2
    print(f'Voce jogou {player} e o computador {pc}. Total de {player + pc} deu ', end='')
    print('PAR' if resto == 0 else 'IMPAR')
    print('-' * 40)
    if resto == 0:
        if escolha == 'P':
            print('Voce VENCEU!\nVamos jogar novamente...')
            vit += 1
        else:
            print(f'Voce PERDEU!')
            break
    elif resto != 0:
        if escolha == 'P':
            print('Voce PERDEU!')
            break
        else:
            print('VOCE VENCEU!\nVamos jogar novamente...')
            vit += 1
print('=-' * 20)
print(f'GAME OVER!Total de vitorias consecutivas: {vit}.')
