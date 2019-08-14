valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print('-' * 40)
print(f'Voce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {valores}')
print(f'O valor 5 faz parte da lista.' if valores.count(5) > 0 else 'O valor 5 nao faz parte da lista.')
