# Método construtor

class Gato:
  ''' Classe para trabalhar com gatos'''
  def __init__(self, nick): # O método __init__ é o construtor da classe. Ele inicializa o objeto da classe (nesse caso ele define o atributo nick com o nome do gato)
    ''' Inicializa o objeto capturando o nome do animal'''
    self.nick = nick # Armazena o nome do gato como um atributo da instância.
    print('Seu gato se chama', self.nick)

nome_gato = (input('Digite o nome do seu pet: ')) # Solicitando a variável para o usuário
g1 = Gato(nome_gato) # Cria uma instância (objeto) da classe Gato, passando o nome do gato como argumento