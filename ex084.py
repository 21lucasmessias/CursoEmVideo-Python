pessoas = list()
pessoa = list()
op = maisp = menorp = 0
pessoasg = list()
pessoasm = list()

while op != 4:
    try:
        op = int(input(f'Total de pessoasas registradas: {len(pessoas)}\n'
                       '[1] Registrar nova pessoa.\n'
                       '[2] Resultado final.\n'
                       '[3] Sair.\n'
                       '>\t'))
        if op not in (1, 2, 3):
            op += 'str'
    except Exception:
        print('Opcao invalida.')
    else:
        if op == 1:
            pessoa.append(str(input('Nome: ').strip().title()))
            pessoa.append(float(input('Peso: ').strip()))
            if pessoa[1] > maisp or len(pessoas) == 0:
                maisp = pessoa[1]
            if pessoa[1] < menorp or len(pessoas) == 0:
                menorp = pessoa[1]
            pessoas.append(pessoa[:])
            pessoa.clear()
        elif op == 2 and len(pessoas) > 0:
            for p in pessoas:
                if p[1] == maisp:
                    pessoasg.append(p[0])
                if p[1] == menorp:
                    pessoasm.append(p[0])
            print(f'Ao todo, foram registradas {len(pessoas)} pessoas.' if len(pessoas) > 1
                  else print(f'Ao todo, foi registrado {len(pessoas)} pessoa.'))
            print(f'O maior peso foi de {maisp}KG. Peso de {pessoasg}')
            print(f'O menor peso foi de {menorp}KG. Peso de {pessoasm}')
            break
        elif op == 3:
            break
