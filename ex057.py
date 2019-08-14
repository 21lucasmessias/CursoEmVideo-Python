sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
print('Sexo {} registrado.'.format(sexo))
