produtos = ('Lapis', 2.00, 'Caderno', 10.00, 'Borracha', 1.00,
            'Caneta', 3.00, 'Lapiseira', 1000.00)
print(f'''
{'-' * 30}
{'LISTAGEM DE PRECOS':^30}
{'-' * 30}''')
for cont, produto in enumerate(produtos):
    if cont % 2 == 0:
        print(f'{produto:.<19}', end=' ')
    else:
        print(f'R${produto:>8.2f}')
print('-' * 30)
