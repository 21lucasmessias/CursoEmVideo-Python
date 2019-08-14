from datetime import date
idade = date.today().year - int(input('Ano de nascimento: '))
if idade > 18:
    print('Ja se passou {} anos de seu alistamento.'.format(idade - 18))
elif idade == 18:
    print('Esta na hora do seu alistamento.')
else:
    print('Faltam {} anos para o seu alistamento.'.format(18 - idade))
