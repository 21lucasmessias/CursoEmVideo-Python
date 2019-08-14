km = int(input('Velocidade do carro registrada (KM): '))
print('MULTADO em R${:.2f}'.format((km - 80)*7.00) if km > 80 else 'Dirigiu abaixo de 80km/h')
