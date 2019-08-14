import random
jogo = list()
n = int(input('Quantos jogos voce quer que eu sorteie? ').strip())
for c in range(n):
    co = 0
    while co < 6:
        num = random.randrange(1, 60)
        if num not in jogo:
            jogo.append(num)
            co += 1
    jogo.sort()
    print(f'Jogo {c+1:2}: {jogo}')
    jogo.clear()
