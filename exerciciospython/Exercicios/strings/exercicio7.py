# Solicita a frase
frase = input('Digite uma frase: ')

# Criando contadores
espacos = 0
vogais = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Percorre cada caractere da frase
for caractere in frase:
  if caractere == ' ':
    espacos += 1 # Conta espaços em branco
  elif caractere.lower() in vogais: # Verifica se é vogal. A função "lower()" converte uma letra para minúscula
    vogais[caractere.lower()] += 1 # Adiciona a contagem da vogal


print(f'Espaços: {espacos}')
print(f'Vogais:')
for vogal, quantidade in vogais.items(): # Percorre o dicionário vogais e calcula a contagem de cada vogal encontrada na frase
  print(f'{vogal}: {quantidade}')