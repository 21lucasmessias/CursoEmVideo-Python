from datetime import date
idade = date.today().year - int(input('Ano de nascimento: '))
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JUNIOR.')
elif idade <= 20:
    print('SENIOR.')
else:
    print('MASTER.')
