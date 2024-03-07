#Exercicio que valor em metros e é convertido em centimetros, e centimetros em milimetros.
valor = float(input('Insira o metros : '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
cm = valor * 100
mm = valor * 1000
print('O valor em metros : {}  \nO valor  em km : {}  \nO valor  em hm : {}  \nO valor  em dam : {} \nO valor  em cm : {} \nO valor  em mm : {} '.format(valor,km,hm,dam,cm,mm) )
