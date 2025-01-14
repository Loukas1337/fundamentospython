
nome = input('Digite seu nome: ')

for letra in range(len(nome), 0, -1): #  Cria uma sequência que começa do tamanho da string e vai até 1, removendo 1 por 1
  print(nome[:letra]) # Pega uma parte da string, do início até o índice letra