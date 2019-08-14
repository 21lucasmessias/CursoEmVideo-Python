frase = str(input('Verificar palindromo: ')).strip().replace(' ', '').lower()
tamanho = len(frase)
checar = 0
for c in range(0, tamanho // 2):
    L1 = str(frase[c])
    L2 = str(frase[tamanho - 1 - c])
    if L1 == L2:
        checar += 1
if checar == tamanho // 2:
    print('PALINDROMO')
else:
    print('NAO PALINDROMO')
