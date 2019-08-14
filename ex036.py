valor = float(input('Valor da casa: R$'))
salario = float(input('Salario: R$'))
tempo = int(input('Parcelado em quantos anos: ')) * 12
parcela = valor / tempo
if parcela > (salario * 0.30):
    print('Emprestimo \033[31;mnegado\033[m. Parcela excede 30% do salario.')
else:
    print('Emprestimo pode ser realizado com \033[32;msucesso\033[m.')
    print('Parcela de R${:.2f} em {} anos, total de {} parcelas'.format(parcela, tempo // 12, tempo))
