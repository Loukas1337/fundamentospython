# Definindo a função para descobrir onde o número se encaixa
def numeros(n):
  if n > 0:
    return ('P')
  else:
    return ('N')

# Programa principal
r1 = numeros (20)
r2 = numeros (2)
r3 = numeros (0)
r4 = numeros (-5)

print(f'O resultado para 20: {r1}')
print(f'O resultado para 2: {r2}')
print(f'O resultado para 0: {r3}')
print(f'O resultado para -5: {r4}')