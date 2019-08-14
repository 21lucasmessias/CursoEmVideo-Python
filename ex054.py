from datetime import date
s1 = 0
s2 = 0
ano = date.today().year
for c in range(0, 7):
    idade = ano - int(input('Data de nascimento: '))
    if idade >= 21:
        s1 += 1
    else:
        s2 += 1
print('{} ja atingiram a maioridade.'.format(s1))
print('{} ainda nao atingiram a maioridade.'.format(s2))
