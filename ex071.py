# exemplo 1
print(f'''
{'=' * 30}
{'BANCO CEV':^30}
{'=' * 30}''')
valor = int(input('Que valor voce quer sacar? R$'))
notas50 = notas20 = notas10 = notas1 = 0
while True:
    if valor == 0:
        break
    else:
        notas50 = valor // 50
        valor = valor % 50
        notas20 = valor // 20
        valor = valor % 20
        notas10 = valor // 10
        valor = valor % 10
        notas1 = valor
        valor = 0
print(f'''
Total de {notas50} cédulas de R$50
Total de {notas20} cédulas de R$20
Total de {notas10} cédulas de R$10
Total de {notas1} cédulas de R$1
{'=' * 30}
Volte sempre ao BANCO CEV! Tenha um bom dia!''')

# exemplo 2
print(f'''
{'=' * 30}
        BANCO CEV
{'=' * 30}''')
valor = int(input('Que valor voce quer sacar? R$'))
notas50 = notas20 = notas10 = notas1 = 0
if valor > 0:
    notas50 = valor // 50
    valor = valor % 50
    notas20 = valor // 20
    valor = valor % 20
    notas10 = valor // 10
    valor = valor % 10
    notas1 = valor
    print(f'''
    Total de {notas50} cédulas de R$50
    Total de {notas20} cédulas de R$25
    Total de {notas10} cédulas de R$10
    Total de {notas1} cédulas de R$1
{'=' * 30}
Volte sempre ao BANCO CEV! Tenha um bom dia!''')
