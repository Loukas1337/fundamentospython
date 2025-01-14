# Resolução Renzo

# Criando a classe com os atributos
class Pessoa:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura

# Criando uma função para calcular o crescimento até 21 anos e o envelhecimento
  def envelhecer(self):
    if self.idade < 21:
      self.altura += 0.5
    self.idade += 1 # Aumentando a idade da pessoa até o limite estabelecido (22)

# Criando o objeto
otavio = Pessoa('Otávio', 1, 5, 40)

# Loop para envelhecer Otávio até 22 anos
for _ in range(22):
  otavio.envelhecer()
  print(f'A idade de {otavio.nome} é de {otavio.idade} anos. E sua altura é de {otavio.altura} cm')