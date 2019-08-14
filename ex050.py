s = 0
for c in range(0, 6):
    num = int(input('{}º numero: '.format(c)))
    if num % 2 == 0:
        s += num
print(s)
