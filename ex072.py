extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    numero = int(input('Numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(extenso[numero])
        opcao = ' '
        while opcao not in 'SN':
            opcao = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if opcao == 'N':
            break
