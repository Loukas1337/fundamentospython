# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de três e que se encontram no intervalo de 1 a 500.

# Armazenando a soma
soma = 0

for c in range(1, 501):
  if c % 2 != 0 and c % 3 == 0: # Descobrir se o numero é impar; descobrir se o numero é multiplo de 3
    soma += c #Adiciona o número à soma

print (f'A soma dos numeros impares que sao multiplos de 3 e se encontram entre 1 a 500, são: {soma}')