frase = str(input('Frase: '))
print('Quantas vezes aparece a letra A: {}'.format(frase.lower().count('a')))
print('A aparece pela primeira vez na posiçao: {}'.format(frase.find('a')))
print('A aparece pela ultima vez na posiçao: {}'.format(frase.rfind('a')))
