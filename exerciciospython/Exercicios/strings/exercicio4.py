
nome = input('Digite seu nome: ')

for letra in range(1, len(nome) + 1): # Percorrendo de 1 até o comprimento do nome
  print(nome[:letra]) # Pega uma parte da string, do início até o índice "letra"