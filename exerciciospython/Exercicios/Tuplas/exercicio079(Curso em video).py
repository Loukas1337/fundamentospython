# Criando uma lista para armazenar os valores dado pelo usuário
valores = []

# Criando um laço para perguntar ao usuário os valores
while True:
  n = int(input('Digite um número: '))
  if n not in valores:
    valores.append(n)
    print('Valor adicionado com sucesso!')
  else:
    print('Valor já existente. Não será adicionado.')
  r = str(input('Quer continuar? S/N ' )).upper()
  if r in 'Nn':
    break

valores.sort() # Colocando a lista em ordem crescente
print(f'Os números digitados foi/foram: {valores}')