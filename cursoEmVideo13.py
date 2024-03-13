#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''import math
num = float(input('Digite um número real:'))
real = math.trunc(num)
print(f'O número escolhido é :{num},o resultado dele em real {real}',)'''

from math import trunc
num = float(input('Informe um número real:'))
print(f'O valor real é :{num},e o valor inteiro dele sera:{trunc(num)}')
