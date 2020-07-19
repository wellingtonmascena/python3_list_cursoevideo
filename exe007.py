#Exercício 007: Ler duas notas e calcule a média aritmética.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

print('O aluno tirou {:.2f} na primeira nota e {:.2f} na segunda nota. A média do aluno é {:.2f}'.format(nota1, nota2, media))
