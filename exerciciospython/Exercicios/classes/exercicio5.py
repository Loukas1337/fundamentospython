# Métodos gerais

class Gato:
  ''' Classe para trabalhar com gatos '''
  tipo_animal = 'felino'

  def __init__(self, nome):
    ''' Inicializa o objeto capturando o nome do animal '''
    self.nome = nome
    print(f'Seu gato se chama {self.nome}.' )


  def peso_gato(self, peso):
    self.peso = peso
    if (self.peso > 5.0):
      print('Seu gato está inchado')
    elif (self.peso > 3.5):
      print('Peso normal')
    else:
      print('O animal está abaixo do peso')

  def _dieta_especial(self):
    self.msg = 'Tudo ok'
    if (self.peso <3.5):
      self.msg = 'Aumente a ração do felino'
    if (self.peso >5.0):
      self.msg = 'Diminua a ração do felino'
    return self.msg

  def dados_gato(self):
    print(f'\nO gato(a) {self.nome} está com {self.peso} kg')
    print(self._dieta_especial())

nome_gato = input('Digite o nome do seu gato: ')
g1 = Gato(nome_gato)

peso = float(input('\nDigite o peso do seu gato em kg: '))
g1.peso_gato(peso)
g1.dados_gato()