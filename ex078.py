valores = list()
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posiçao {p}: ')))
print('-' * 35)
# 1
print(f'Voce digitou os valores {valores}')
# 2
print(f'O maior valor digitado foi {max(valores)} ', end='')
print('nas posiçoes ' if valores.count(max(valores)) > 1 else 'na posiçao ', end='')
for p, valor in enumerate(valores):
    if valores.count(max(valores)) > 1 and valor == max(valores):
        print(p, end='...')
    elif valores.count(max(valores)) == 1 and valor == max(valores):
        print(p)
# 3
print(f'\nO menor valor digitado foi {min(valores)} ', end='')
print('nas posiçoes ' if valores.count(min(valores)) > 1 else 'na posiçao ', end='')
for p, valor in enumerate(valores):
    if valores.count(min(valores)) > 1 and valor == min(valores):
        print(p, end='...')
    elif valores.count(min(valores)) == 1 and valor == min(valores):
        print(p)
