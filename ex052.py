checar = 0
num = int(input('Checar se o numero é primo: '))
for c in range(1, num+1):
    if num % c == 0:
        print('{} é divisivel por {}'.format(num, c))
        checar += 1
if checar == 2:
    print('Numero primo.')
else:
    print('Numero nao primo.')
