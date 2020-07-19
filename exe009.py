#Exercício 009: programa que retorna a tabuada de um número inteiro lido.

tabuada = int(input('Digite a tabuada desejada: '))
i = 0
print('-'*15)
for i in range(11):
    i = i + 1
    print('{} x {:2} = {}'.format(tabuada,i, tabuada*i ))
print('-'*15)