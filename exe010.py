#Exercício 010: Ler quantia em dinheiro e retornar quantos dólares pode-se comprar.
# Considere US$1.00 = R$3.27

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.20
print('Com R${:.2f} você compra US${:.2f}'.format(real, dolar))