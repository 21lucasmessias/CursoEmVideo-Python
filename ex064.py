num = int(input('Numero [999 para parar]: '))
soma = 0
while num != 999:
    soma += num
    num = int(input('Numero: '))
print('Soma dos numeros digitados: {}'.format(soma))
