from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vale: {:.2f}'.format(hi))
