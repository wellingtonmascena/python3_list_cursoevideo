# Exercicio 04: programa que ler uma entrada do teclado  e mostre na tela seu tipo primitivo e todas informações sobre o tipo

entrada = input('Digite algo: ')

print('O tipo primitivo desse valor é ',type(entrada))
print('Só tem espaços? ',entrada.isspace())
print('É um número:',entrada.isnumeric())
print('É alfabético? ',entrada.isalpha())
print('É alfanumérico? ',entrada.isalnum())
print('É maiúsculo?', entrada.upper())
print('É minusculo?', entrada.islower())
print('É capitalizado?',entrada.istitle())
