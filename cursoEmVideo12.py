#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.

km = float(input('Quantos km rodados :'))
dias = int(input('Por quantos dias ele foi alugado : '))
pagamento = (km * 0.15) + (dias * 60)
print('O total a pagar R$:{:.2f}'.format(pagamento))
