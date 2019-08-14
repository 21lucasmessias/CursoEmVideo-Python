salario = float(input('Salario atual: R$'))
if salario >=1250:
    print('Seu salario +10% agora vale : R${:.2f}'.format(salario*1.10))
else:
    print('Seu salario +15% agora vale : R${:.2f}'.format(salario*1.15))
