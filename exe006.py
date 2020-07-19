#Exercício 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero **(1/2)

print('O dobro de {} é {}.'.format(numero, dobro))
print('O triplo de {} é {}.'.format(numero,triplo))
# Como a operação de raiz quadrada retorna um flutuante podemos colocar .2f para o flutuante
print('A raiz quadrada de {} é {:.2f}.'.format(numero,raizQuadrada))
print('A raiz quadrada de {} é {:.2f} usando a função pow()'.format(numero,pow(numero,0.5)))