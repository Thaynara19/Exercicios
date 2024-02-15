#Exercicio faça um programa que leia a largura e a altura de uma parede em metros,calcule sua area e a quantidade de tinta necessaria para pintalo,sabendo que cada litro de tinta,pinta uma area de 2m².

largura = float(input('Informe a largura em metros :'))
altura = float(input('Informe a area :'))
area = largura * altura
pintura = area / 2

print('A sua largura é : {} e sua area é : {} o  valor total : {}'.format(largura,altura,area) )
print('A quantidade de tinta necessaria é :',pintura)
