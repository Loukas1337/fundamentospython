
# Criando uma classe
class Quadrado:
  def __init__(self, tamanho_do_lado):
    self.tamanho_do_lado = tamanho_do_lado

  def mudar_valor(self, novo_tamanho):
    self.tamanho_do_lado = novo_tamanho

  def mostra_lado(self):
    return self.tamanho_do_lado

  def retornar_valor(self):
    return self.tamanho_do_lado

  def calcular_area(self):
    area = self.tamanho_do_lado * self.tamanho_do_lado
    return area


# Exemplo de uso
lado1 = Quadrado(3)
print(f'O lado inicial é {lado1.mostra_lado()}')


# Alterando o lado do quadrado
lado1.mudar_valor(4)


# Retornando o valor do lado alterado
print(f'O lado atualizado é {lado1.retornar_valor()}')


# Calculando e mostrando a área do quadrado
print(f'A área do quadrado é {lado1.calcular_area()}')