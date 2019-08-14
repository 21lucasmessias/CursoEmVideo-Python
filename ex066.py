soma = cont = 0
while True:
    num = int(input('Valor inteiro [999 para sair]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma vale {soma}.\nForam digitados {cont} numero(s).')
