# Criando uma classe
class Retangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def mudar_valor(self, nova_base, nova_altura):
    self.base = nova_base
    self.altura = nova_altura

  def mostra_base(self):
    return self.base

  def mostra_altura(self):
    return self.altura

  def retornar_valor(self):
    return self.base, self.altura

  def perimetro(self):
    return 2 * (self.base + self.altura)

  def calcular_area(self):
    area = self.base * self.altura
    return area

# Exemplo de uso
retangulo = Retangulo(3, 4)

print(f'A base inicial é {retangulo.mostra_base()}')
print(f'A altura inicial é {retangulo.mostra_altura()}')

# Alterando a base e a altura do retângulo
retangulo.mudar_valor(5, 6)

# Retornando os valores atualizados da base e da altura
print(f'O valor atualizado da base e altura é {retangulo.retornar_valor()}')

# Calculando e mostrando o perímetro
print(f'O perímetro do retângulo é {retangulo.perimetro()}')


# Calculando e mostrando a área do retângulo
print(f'A área do retângulo é {retangulo.calcular_area()}')