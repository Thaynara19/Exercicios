#Exercicio crie um algoritmo que leia um número e mostre seu dobro,trilo e raiz quadrada.
#pow pode ser usado para descobrir a raiz quadrada pow(n, (1/2)
numero = int(input('Informe um número : '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print('Valor do dobro : {} , valor do triplo : {} , e o valor da raiz quadrada : {:.2f}'.format(dobro,triplo,raiz))
