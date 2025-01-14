# Variáveis de Classe e de Instância

# Criando a classe
class Gato:
  tipo_animal = 'felino' # Variável de classe. O valor pode ser compartilhado para todos, para um ou para alguns objetos. A variável de classe pode ser alterada no decorrer do código, e alterada também para um objeto em específico caso seja necessário

  def __init__(self, nome):
    self.nome = nome # Variável de instância. Ela é diferente para cada um dos objetos


# Alterando o valor da variável de classe
Gato.tipo_animal = 'pet'

# Criando os objetos
g1 = Gato('Nino')
g2 = Gato('Bibi')

# Apresentando que a variável de classe é o mesmo valor, independente do objeto
print(g1.tipo_animal)
print(g2.tipo_animal)

# Apresentando a variável de instância para cada objeto
print(g1.nome)
print(g2.nome)

# Alterando a variável de classe para um objeto em particular
g1.tipo_animal = 'bichano'
print(g1.tipo_animal)
print(g2.tipo_animal)