matriz = list()
linha = list()
for l in range(3):
    for n in range(3):
        linha.append(int(input(f'Digite um valor para [{l}, {n}]: ')))
    matriz.append(linha[:])
    linha.clear()
for l in matriz:
    for n in l:
        print(f'[ {n} ]', end='')
    print('')
