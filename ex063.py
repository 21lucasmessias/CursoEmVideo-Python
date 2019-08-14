termos = int(input('Numero de termos de fibonacci: '))
fib1 = 0
fib2 = 1
print(fib1)
print(fib2)
while termos > 0:
    print('{}'.format(fib1 + fib2))
    fib0 = fib1
    fib1 = fib2
    fib2 = fib0 + fib2
    termos -= 1
