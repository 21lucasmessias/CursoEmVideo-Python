valores = list()
valorespares = list()
valoresimpares = list()
while True:
    valores.append(int(input('Digite um numero: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
for valor in valores:
    if valor % 2 == 0:
        valorespares.append(valor)
    else:
        valoresimpares.append(valor)
print('-' * 40)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {valorespares}')
print(f'A lista de impares é {valoresimpares}')