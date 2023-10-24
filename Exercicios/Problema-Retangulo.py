import math

base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))

area = base * altura
perimetro = (base * 2) + (altura * 2)
diagonal = math.sqrt(base ** 2 + altura **2)
print()
print('O valor da area é: ', area)
print()
print('O valor do perimetro é: ', perimetro)
print()
print('O valor da diagonal é: ', diagonal)