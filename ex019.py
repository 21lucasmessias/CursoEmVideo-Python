from random import choice
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
r = choice(lista)
print(r)
