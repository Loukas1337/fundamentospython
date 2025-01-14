# Variável para acumular a soma dos numeros à medida em que o usuário insere
soma = 0

# Solicitando os 5 numeros ao usuário
for c in range(5):
  numero = float(input(f"Digite o {c+1}º número: "))

# Acumulando o valor
  soma += numero

# Calculando a média
media = soma / 5

# Retornando a soma e a média para o usuário
print(f'A soma dos numeros é {soma}')
print(f'A media dos numeros é {media}')