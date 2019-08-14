import random
num = random.randint(0, 5)
n = int(input('Descubra qual o numero secreto entre 0 e 5: '))
print('Acertou mizeravi' if n == num else 'Erooou, o numero era: {}'.format(num))
