from random import randint
pc = randint(0, 10)
cont = 0
jogador = int(input('Tente adivinhar o numero que eu pensei entre 0 e 10: '))
while jogador != pc:
    if jogador > pc:
        jogador = int(input('MENOS! Tente novamente: '))
    if jogador < pc:
        jogador = int(input('MAIS! Tente novamente: '))
    cont += 1
print('ACERTOU! O numero é {}.\nTotal de {} tentativas.'.format(pc, cont))
