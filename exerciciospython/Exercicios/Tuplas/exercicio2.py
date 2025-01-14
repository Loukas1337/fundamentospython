# Armazenando uma lista para receber os numeros fornecidos pelo usuário
lista = []

# Criando a solicitação dos numeros e adicionando na lista
for i in range(10):
  n = float(input(f'Digite o numero {i+1}: '))
  lista.append(n)

print("Lista na ordem inversa:")

# Mostrando a lista inversa
lista.reverse()
print(lista)

# Outra forma de deixar a lista inversa
for i in range(9, -1, -1):
  print(lista[i])