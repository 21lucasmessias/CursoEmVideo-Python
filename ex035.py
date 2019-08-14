t1 = float(input('Reta 1: '))
t2 = float(input('Reta 2: '))
t3 = float(input('Reta 3: '))
if (t1 + t2) > t3 and (t1 + t3) > t2 and (t2 + t3) > t1:
    print('Os segmentos PODEM formar um triangulo.')
else:
    print('Os segmentos NAO PODEM formar um triangulo.')
