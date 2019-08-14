n1 = float(input('1º numero: '))
n2 = float(input('2º numero: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 == n2:
    print('{} é igual a {}'.format(n1, n2))
else:
    print('{} é menor que {}'.format(n1, n2))
