produto = float(input('Preço produto: '))
opcao = int(input('''Escolha uma opçao:
[1] A vista (dinheiro/choque). 10% desconto.
[2] A vista (cartao). 5% desconto.
[3] 2x (cartao). Preço normal.
[4] 3x ou mais (cartao). 20% de juros.\n'''))
if opcao == 1:
    print('Total de \033[31;mR${:.2f}\033[m'.format(produto * 0.90))
elif opcao == 2:
    print('Total de \033[31;mR${:.2f}\033[m'.format(produto * 0.95))
elif opcao == 3:
    print('Total de \033[31;mR${:.2f}\033[m'.format(produto))
elif opcao == 4:
    print('Total de \033[31;mR${:.2f}\033[m'.format(produto * 1.20))
else:
    print('Opcao invalida.')