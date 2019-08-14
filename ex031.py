viagem = int(input('Quantidade em kilometros da sua viagem: '))
print('Total R${}'.format(viagem*0.50) if viagem < 200 else 'Total R${}'.format(viagem*0.45))
