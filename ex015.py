km = float(input('Km rodados: '))
dias = int(input('Total de dias que o carro foi alugado: '))
print('Total de preço a pagar: R${:.2f}'.format((dias * 60) + (km * 0.15)))
