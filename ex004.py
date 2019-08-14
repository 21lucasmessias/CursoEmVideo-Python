algo=input('Digite algo para ser verificado: ')

print('{} é '.format(algo), type(algo))
print('{} é alpha-numerico? '.format(algo), algo.isalnum())
print('{} é alpha? '.format(algo), algo.isalpha())
print('{} é decimal? '.format(algo), algo.isdecimal())
print('{} esta em letras minusculas? '.format(algo), algo.islower())
print('{} esta em letras maisculas? '.format(algo), algo.isupper())