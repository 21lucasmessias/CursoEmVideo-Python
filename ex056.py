media = 0
f = 0
fm = 0
maior = 0
velho = 'Nenhuma pessoa do sexo masculino foi inscrita.'
for c in range(0, 4):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().lower()
    media += idade
    if sexo == 'm' and idade > maior:
        maior = idade
        velho = nome
    elif sexo == 'f':
        f += 1
        if idade < 20:
            fm += 1
print('Media de idade do grupo {:.2f}.'.format(media / 4))
print('O homem mais velho se chama {}'.format(velho))
print('total de mulheres com menos de 20 anos {}.'.format(fm))
