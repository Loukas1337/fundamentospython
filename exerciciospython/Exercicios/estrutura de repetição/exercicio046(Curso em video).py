# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

# Definindo o valor inicial da contagem

inicio = 10

# Loop para contagem regressiva

for i in range(inicio, -1, -1):
    print(i)
    time.sleep (1)  # Pausa de 1 segundo entre os números

print('A bomba explodiu!')