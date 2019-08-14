lista = list()
for item in range(0, 5):
    valor = int(input('Digite um valor: '))
    if item == 0:
        lista.append(valor)
        print('O item foi adicionado no final da lista.')
    else:
        posicao = 0
        for i in range(0, len(lista)):
            if valor > lista[i]:
                posicao += 1
            else:
                break
        lista.insert(posicao, valor)
        print(f'O valor {valor} foi adicionado na posiçao {posicao} da lista...')
print('-' * 50)
print(f'Os valores digitados em ordem foram {lista}')
