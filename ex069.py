demaior = homens = mulheresdemenor = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)
    if idade >= 18:
        demaior += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheresdemenor += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'''{'-' * 30}
{'=' * 5} FIM DO PROGRAMA {'=' * 5}
Total de pessoas com mais de 18 anos: {demaior}.
Total de homens cadastrados: {homens}.
Total de mulheres com menos de 20 anos: {mulheresdemenor}''')
