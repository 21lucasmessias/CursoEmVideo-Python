condwhile = int(input('Numero a ser fatorado em while: '))
fatorialwhile = 1
while condwhile > 0:
    print('{}'.format(condwhile), end='')
    print(' x ' if condwhile > 1 else ' = ', end='')
    fatorialwhile = fatorialwhile * condwhile
    condwhile -= 1
print(fatorialwhile, '\n')

numerofor = int(input('Numero a ser fatorado em for: '))
condfor = numerofor
fatorialfor = 1
for condfor in range(condfor, 0, -1):
    print('{}'.format(condfor), end='')
    print(' x ' if condfor > 1 else ' = ', end='')
    fatorialfor *= condfor
print(fatorialfor)
