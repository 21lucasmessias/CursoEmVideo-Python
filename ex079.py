lista = list()

while True:
    num = int(input('Numero: '))
    if num in lista:
        print('Numero repetido. Nao irei adicionar.')
    else:
        lista.append(num)
        print('Numero adicionado com sucesso!')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
lista.sort()
print(lista)
