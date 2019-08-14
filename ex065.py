opcao = 's'
cont = media = maior = menor = 0
while opcao not in 'nN':
    opcao = str(input('Digitar mais um valor?[S/N]')).strip()
    if opcao in 'sS':
        num = float(input('Valor: '))
        if cont == 0:
            menor = maior = num
        if num < menor:
            menor = num
        elif num > maior:
            maior = num
        cont += 1
        media += num
    elif opcao not in 'sSnN':
        print('Opcao invalida.')
if media > 0:
    print('Media dentre os numeros: {:.2f}'.format(media/cont))
    print('Menor numero {}'.format(menor))
    print('Maior numero {}'.format(maior))
else:
    print(0)
