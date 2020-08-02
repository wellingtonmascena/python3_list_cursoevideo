#Exercício 011: Ler largura e altura de uma parade em metros, calcular a sua área e a quantidade de tinta necessária para pintar.
#OBS: 1 litro de tinta pinta 2 metros quadrados de parede.

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area / 2
print('Você precisa de {:.2f} litros de tinta para pintar sua parede {:.2f}x{:.2f} com {:.2f} metros quadrados de parede'.format(tinta, altura, largura, area))