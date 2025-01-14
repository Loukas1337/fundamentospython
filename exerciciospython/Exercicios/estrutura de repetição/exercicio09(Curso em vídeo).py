# Faça um programa que leia um numero inteiro qualquer e mostre a sua tabuada.

n = int(input('Digite um numero para ver a tabuada do mesmo: '))

for t in range(0, 11):
  resultado = n * t
  print(f'{n} x {t} = {resultado}')