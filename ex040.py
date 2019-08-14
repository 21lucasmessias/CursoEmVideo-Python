n1 = float(input('1º nota: '))
n2 = float(input('2º nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado.')
elif media < 6.9:
    print('Recuperaçao.')
else:
    print('Aprovado.')
