aluno = {}
aluno['Nome'] = str(input("Nome: "))
aluno['Media'] = float(input("Media: "))
if aluno['media'] >= 7:
    aluno['Situacao'] = "Aprovado"
for k, v in aluno.items():
    print(f"{k} eh igual a {v}")

