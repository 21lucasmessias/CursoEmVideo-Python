opcao = 0
valor1 = 0
valor2 = 0
while opcao != 5:
    opcao = int(input('''
    Menu
Valores atuais: {} e {}.
[1]Somar.
[2]Multiplicar.
[3]Maior.
[4]Novos numeros.
[5]Sair do programa.
Opcao: '''.format(valor1, valor2)))
    if opcao == 1:
        print('{} + {} = {}'.format(valor1, valor2, valor1 + valor2))
    elif opcao == 2:
        print('{} * {} = {}'.format(valor1, valor2, valor1 * valor2))
    elif opcao == 3:
        if valor1 > valor2:
            print('{} é maior que {}'.format(valor1, valor2))
        elif valor1 == valor2:
            print('Os numeros sao iguais.')
        else:
            print('{} é maior que {}'.format(valor2, valor1))
    elif opcao == 4:
        valor1 = float(input('Novo valor 1: '))
        valor2 = float(input('Novo valor 2: '))
    elif opcao != 5:
        print('Opcao invalida.')
