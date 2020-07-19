#Exercício 008: Programa que ler um valor em metros e exibe convertido em centímetros e milímetros

valorMetros = float(input('Digite o valor em metros: '))

valorcm = valorMetros * 100
valormm = valorMetros * 1000

print('O valor de {:.2f}m corresponde a {:.2f}cm e {:.2f}mm.'.format(valorMetros,valorcm,valormm))