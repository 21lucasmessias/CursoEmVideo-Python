palavras = ('Adoleta', 'Lepeti', 'Peti', 'Pola', 'Hamburguer',
            'Cafe', 'Aprender', 'Programar', 'LiNgUaGem',
            'PyThon')
for palavra in palavras:
    print(f'{"Na palavra " + palavra + " temos:" :30} ', end='')
    palavra = palavra.lower().strip()
    for vogal in palavra:
        if vogal in 'aeiou':
            print(vogal, end=' ')
    print('')
