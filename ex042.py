r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    if r1 == r2 == r3:
        print('Triangulo equilatero. Todos os lados iguais.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triangulo isosceles. Dois lados iguais.')
    elif r1 != r2 != r3 != r1:
        print('Triangulo escaleno. Todos os lados diferentes.')
    else:
        print('Triangulo desconhecido.')
else:
    print('Essas tres retas nao formam um triangulo.')
