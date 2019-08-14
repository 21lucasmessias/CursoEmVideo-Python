print(f'''
{'-' * 30}
      LOJA SUPER BARATAO
{'-' * 30}
''')
contp = soma = pmbp = caros= 0
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    contp += 1
    if contp == 0 or preco < pmbp:
        pmbn = produto
        pmbp = preco
    if preco > 1000:
        caros += 1
    soma += preco
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'''
{'FIM DO PROGRAMA':-^30}
O total de compra foi R${soma:.2f}
Temos {caros} produtos custando mais de R$1000.00
O produto mais barato foi {pmbn} que custa R%{pmbp:.2f}''')
