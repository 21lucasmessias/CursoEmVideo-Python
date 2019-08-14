import emoji
from random import randint
from time import sleep

player = int(input(emoji.emojize('''   \033[1;34;mEscolha sua jogada
     [1]  :v:   [1]
     [2]  :fist:  [2]
     [3]  :hand:  [3]\033[m
          ''', use_aliases=True)))

if player == 1:
    jogada_player = ':v:'
elif player == 2:
    jogada_player = ':fist:'
else:
    jogada_player = ':hand:'

pc = randint(1, 3)

if pc == 1:
    jogada_pc = ':v:'
elif pc == 2:
    jogada_pc = ':fist:'
else:
    jogada_pc = ':hand:'

print(emoji.emojize('\n ===== '
                    '\033[1;34;m{} '
                    '\033[1;mVS '
                    '\033[1;31;m{}'
                    '\033[m ====='.format(jogada_player, jogada_pc), use_aliases=True))

if (player == 1 and pc == 1) or (player == 2 and pc == 2) or (player == 3 and pc == 3):
    print('     \033[1;31;m!!!EMPATE!!!\033[m')
elif (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
    print('     \033[1;31;m!!!PERDEU!!!\033[m')
elif (player == 1 and pc ==3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
    print('     \033[1;31;m!!!VENCEU!!!\033[m')
else:
    print('Erro.')
print('=' * 22)
