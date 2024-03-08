#Exercicio que um programa vai ler o valor que tem na carteira e mostre o resultado em dolares que ele pode comprar.

real = float(input('Quanto dinheiro você tem na carteira ? R$ '))
dolar = real / 3.27
print('O valor que você tem na carteira R$ : {:.2F} ,você pode comprar US$ : {:.2f} '.format(real,dolar))
