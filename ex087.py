matriz = list()
linha = list()
par = 0
for l in range(3):
    for n in range(3):
        linha.append(int(input(f'Digite um valor para [{l}, {n}]: ')))
    matriz.append(linha[:])
    linha.clear()
for l in matriz:
    for n in l:
        if n % 2 == 0:
            par += n
        print(f'[ {n} ]', end='')
    print('')
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da tarceira coluna é {matriz[0][2] + matriz [1][2] + matriz [2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')