
# Perguntando as variáveis
populacao_a = float(input('Qual a população do país A? '))
populacao_b = float(input('Qual a população do país B? '))
taxa_a = float(input('Qual a taxa de crescimento do país A? '))
taxa_b = float(input('Qual a taxa de crescimento do país b? '))

# Contador de anos
anos = 0

# Laço até população de A ultrapassar a de B
while populacao_a < populacao_b:
  populacao_a = populacao_a * taxa_a
  populacao_b = populacao_b * taxa_b
  anos += 1

# Número de anos necessários
print(f'Serão necessários {anos} ano(s) para que a população do país A ultrapasse a do país B.')