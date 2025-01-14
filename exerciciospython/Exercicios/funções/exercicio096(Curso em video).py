# Solicitando as variáveis
l = float(input('Qual a largura do terreno (em metros)? '))
c = float(input('Qual o comprimento do terreno (em metros)? '))
#
area(l, c)

# Criando a função e devolvendo o resultado
def area(l, c):
  area = l * c
  print(f'A área do terreno {l} x {c} é de {area} m²')