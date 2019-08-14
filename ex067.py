while True:
    print('-' * 40)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    mult = 0
    while True:
        mult += 1
        if mult == 11:
            break
        print(f'{valor:2} x {mult:2} = {valor * mult:2}')
