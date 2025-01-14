# Informações dadas pela pergunta
populacao_a = 80000
populacao_b = 200000
taxa_a =  1.03
taxa_b = 1.015

# Contador de anos
anos = 0

# Laço até população de A ultrapassar a de B
while populacao_a < populacao_b:
  populacao_a = populacao_a * taxa_a
  populacao_b = populacao_b * taxa_b
  anos += 1

# Número de anos necessários
print(f'Serão necessários {anos} anos para que a população do país A ultrapasse a do país B.')