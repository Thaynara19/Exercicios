#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input("Informe o Ângulo :"))

se = math.asin(math.radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f} ".format(angulo,se))

cos = math.cos(math.radians(angulo))
print("O ângulo de {} tem o COSSENO de {:.2f} ".format(angulo,cos))

tg = math.tan(math.radians(angulo))
print("O ângulo de {} tem o TANGENTE de {:.2f} ".format(angulo,tg))
