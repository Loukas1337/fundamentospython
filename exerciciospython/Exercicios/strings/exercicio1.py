# Solicitando a string para o usuário
str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

# Programa principal onde se verifica se são iguais e se possuem o mesmo conteúdo
def comparacao_strings(str1, str2):
  print(f'String 1: {str1}, (tamanho: {len(str1)})')
  print(f'String 2: {str2}, (tamanho: {len(str2)})')

  if len(str1) == len(str2):
    print('Elas possuem o mesmo tamanho.')
  else:
    print('Elas possuem tamanhos diferentes.')

  if str1 == str2:
    print('Elas possuem o mesmo conteúdo.')
  else:
    print('Elas possuem conteúdos diferentes.')

# Chamando a função
comparacao_strings(str1, str2)