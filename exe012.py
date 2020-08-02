#Exercício 012: Calculando descontos lendo o preço e motre o seu novo preço, com desconto de 5%

valorProduto = float(input('Digite o valor do produto: '))
desconto = 5
valorDesconto =valorProduto - (valorProduto*desconto/100)
print('Seu produto de valor R$ {:.2f} com {:.2f}% de desconto fica R${:.2f}.'.format(valorProduto, desconto, valorDesconto))