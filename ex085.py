par = list()
impar = list()
numeros = (par, impar)
c = 0

while c < 7:
    try:
        num = (int(input(f'{c + 1}º Numero: ').strip()))
        if num % 2 == 0 and num not in par:
            par.append(num)
        elif num % 2 != 0 and num not in impar:
            impar.append(num)
        c += 1
    except Exception:
        print('Erro.')

par.sort()
impar.sort()

if par[0] < impar[0]:
    print(numeros)
else:
    print(numeros[1], numeros[0])
