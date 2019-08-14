
expressao = list(input('Digite a expressao: '))
check = list()
resposta = 'Sua expressao esta correta!'
for e, l in enumerate(expressao):
    if l == '(':
        if len(expressao) - 1 == e:
            resposta = 'Sua expressao esta errada!'
            break
        else:
            check.append(l)
    elif l == ')':
        if len(check) > 0:
            del check[0]
        else:
            resposta = 'Sua expressao esta errada!'
            break
if len(check) > 0:
    resposta = 'Sua expressao esta errada!'
print(resposta)
