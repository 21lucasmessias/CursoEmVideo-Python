num = int(input('Numero a ser tabuado: '))
for c in range(1, 11):
    print('{} x {:2} = {:3}'.format(num, c, num * c))
