# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


# Resolução Renzo

import math

area_a_ser_pintada = int(input('Digite a área, em metros quadrados a ser pintada: ')) # area em metros quadrados
area_com_folga = area_a_ser_pintada * 1.1

litros_por_metro = 6

litros_a_serem_usados = area_com_folga / litros_por_metro

litros_por_lata = 18

numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_lata)

valor_com_apenas_latas = numero_de_latas * 80

print (f'Você deverá usar {numero_de_latas} lata(s) de 18 litros, no valor de R$ {valor_com_apenas_latas}')
litros_por_galao = 3.6

numero_de_galoes = math.ceil (litros_a_serem_usados / litros_por_galao)

valor_com_apenas_galoes = numero_de_galoes * 25

print (f'Você deverá usar {numero_de_galoes} galão(ões) de 3.6 litros, no valor de R$ {valor_com_apenas_galoes}')

# Compra de tinta otimizada por valor

numero_de_latas = math.floor (litros_a_serem_usados / litros_por_lata)

valor_de_latas = numero_de_latas * 80

litros_faltantes = litros_a_serem_usados % litros_por_lata

numero_de_galoes = math.ceil(litros_faltantes / litros_por_galao)

valor_com_galoes = numero_de_galoes * 25

valor_total = valor_de_latas + valor_com_galoes