
# Criando a função
def escreva(msg):
  tam = len(msg) + 4 # Determinando o tamanho da linha e colocando uma folguinha com o +4
  print('-' * tam)
  print(f'  {msg}')
  print('-' * tam)


# Programa principal
escreva('Olá, mundo!')
escreva('Estudando fundamentos básicos')