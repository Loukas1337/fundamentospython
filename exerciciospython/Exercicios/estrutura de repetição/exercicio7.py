maximo = float(input('Digite um numero:'))

for i in range(4):
  maximo = max(maximo, float(input('Digite um numero:')))
  print(f'O maior numero encontrato até agora é: {maximo}')


# Outra forma de resolver

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Lê 5 números do usuário
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Encontra o maior número da lista
maior_numero = max(numeros)

# Exibe o maior número
print(f"O maior número é: {maior_numero}")