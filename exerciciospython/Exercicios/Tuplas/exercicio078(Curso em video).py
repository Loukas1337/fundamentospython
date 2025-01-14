# Criando uma lista para armazenar os valores dado pelo usuário
valores = []

# Coletando os valores do usuário
for i in range(5):
  n = int(input(f'Digite um numero {i+1}: '))
  valores.append(n)

# Encontrando o maior número fornecido
maior_numero = max(valores)
print (f'O maior numero é: {maior_numero}')

# Encontrando a posição do maior numero
posicao_maior = valores.index(maior_numero)

# Encontrando o menor número fornecido
menor_numero = min(valores)
print (f'O menor numero é: {menor_numero}')

# Encontrando a posição do menor numero
posicao_menor = valores.index(menor_numero)

print(f'Os valores são {valores}')
print(f'A posição do maior numero é {posicao_maior}')
print(f'A posição do menor numero é {posicao_menor}')