peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('\033[1;31;mAbaixo do peso.\033[m')
elif imc < 25:
    print('\033[1;36;mPeso ideal.\033[m')
elif imc < 30:
    print('\033[1;33;mSobrepeso.\033[m')
elif imc < 40:
    print('\033[1;35;mObesidade.\033[m')
elif imc >= 40:
    print('\033[1;31;mObesidade morbita.\033[m')
else:
    print('Erro.')
