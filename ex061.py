termo = float(input('Primeiro termo: '))
razao = float(input('Razao da PA: '))
termos = 10
while termos > 0:
    print('{} -> '.format(termo), end='')
    termo += razao
    termos -= 1
print('FIM')
