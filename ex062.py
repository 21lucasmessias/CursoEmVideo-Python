termo = float(input('Primeiro termo: '))
razao = float(input('Razao da PA: '))
termos = 10
while termos > 0:
    print('{}'.format(termo))
    termo = termo + razao
    termos -= 1
    if termos == 0:
        termos = int(input('Apresentar + quantos termos?\n'))
