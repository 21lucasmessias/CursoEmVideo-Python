alunos = list()
aluno = list()
notas = list()
media = 0
op0 = ''
while op0 != 'n':
    while op0 != 'n':
        try:
            aluno.append(str(input('Nome: ')).strip().title())
            notas.append(float(input('Nota 1: ').strip()))
            notas.append(float(input('Nota 2: ').strip()))
        except Exception:
            print('Erro.')
        else:
            if notas[0] > 10.0 or notas[1] > 10 or notas[0] < 0 or notas[1] < 0 or len(aluno[0]) == 0:
                print('Erro.')
                notas.clear()
                aluno.clear()
                break
            aluno.append(notas[:])
            aluno.append(((notas[0] + notas[1]) / 2))
            alunos.append(aluno[:])
            aluno.clear()
            notas.clear()
            op0 = str(input('Quer continuar?\n>\t')).strip().lower()[0]
print(f'''No. NOME\t   Media
{'-' * 20}''')
for e, a in enumerate(alunos):
    print(f'{e + 1:<4}{a[0]:12}{a[2]:3.1f}')
op1 = 1
while True:
    try:
        op1 = int(input('Mostrar notas de qual aluno? (0 interrompe)').strip()) - 1
        if op1 == -1:
            break
        print(f'Notas de {alunos[op1][0]} sao {alunos[op1][1]}')
    except Exception:
        print('Erro.')
