numeros = int(input('Digite um numero: ')),\
          int(input('Digite outro numero: ')),\
          int(input('Digite mais um numero: ')),\
          int(input('Digite o ultimo numero: '))
print(f'Voce digitou os valores: {numeros} .')
# 1
print(f'O valor 9 apareceu {numeros.count(9)} {"vez." if numeros.count(9) == 1 else "vezes."}')
# 2
if 3 in numeros:
    print(f'O valor 3 aparece na {numeros.index(3) + 1}º posiçao.')
else:
    print('O valor 3 nao foi encontrado.')
# 3
cont = 0
for numero in numeros:
    if numero % 2 == 0:
        cont += 1
if cont > 0:
    print('Os valores pares digitados foram: ', end='')
    for numero in numeros:
        if numero % 2 == 0:
            print(numero, end=' ')
else:
    print('Nao houve numeros pares digitados.')
