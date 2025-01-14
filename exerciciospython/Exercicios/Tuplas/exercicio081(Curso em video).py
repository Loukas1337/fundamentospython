# Criando uma lista para armazenar os valores dado pelo usuário
valores = []

# Criando um laço para solicitar os números ao usuário
while True:
  n = int(input('Digite um número: '))
  if n not in valores:
    valores.append(n)
    print('Valor adicionado com sucesso.')
  r = str(input('Deseja continuar? S/N ')).upper()
  if r in 'Nn':
    break

print(f'A lista na ordem de preenchimento foi: {valores}')
valores.sort(reverse=True) # Deixando a lista em ordem decrescente
print(f'A lista do(s) números computados em ordem decrescente é: {valores}')
print(f'A quantidade de números computados é {len(valores)}.') # Contando quantos números foram inseridos na lista

# Verificando se o número 5 aparece na lista
if 5 in valores:
  print('O número 5 está na lista.')
else:
  print('O número 5 não está na lista.')