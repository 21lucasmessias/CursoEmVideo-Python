numero = int(input('Numero a ser convertido: '))
opcao = int(input('''Escolha uma opçao:
1.Converter para binario.
2.Converter para octal.
3.Converter para hexadecimal.
'''))
if opcao == 1:
    print(bin(numero)[2:])
elif opcao == 2:
    print(oct(numero)[2:])
elif opcao == 3:
    print(hex(numero)[2:])
else:
    print('Opcao invalida.')
