# Resolução Renzo

# Criando função
def imprimir_triangulo_de_numeros_crescentes(n: int):
  for linha in range(1, n + 1): # Cria o loop de 1 até n, representado na linha atual
    for coluna in range(1, linha + 1): # Percorre as colunas de 1 até o número da linha atual
      print(coluna, end= '  ') # Imprime o número atual (coluna) na mesma linha, com um espaço extra entre os números
    print('') # Adiciona uma nova linha após imprimir todos os números da linha atual.


print('Triângulo com 1')
imprimir_triangulo_de_numeros_crescentes(1)
print('Triângulo com 2')
imprimir_triangulo_de_numeros_crescentes(2)
print('Triângulo com 3')
imprimir_triangulo_de_numeros_crescentes(3)


#-----------------------------------------------------------------

# Outra forma de resolver

def imprimir_triangulo(n: int): # O motivo de especificar n como um inteiro, é para deixar o cód mais legível e dizer que esperamos que o número de entrada seja inteiro
    for linha in range(1, n + 1): # Percorre as linhas de 1 até n
        for coluna in range(1, linha + 1): # Imprime os números da coluna, que vai de 1 até o número da linha atual
            print(coluna, end='  ')  # Imprime os números na mesma linha, separados por dois espaços
        print('')  # Quebra de linha após cada linha de números

# Solicitando número para o usuário
n = int(input("Informe um número inteiro: "))

# Imprimir o triângulo chamando a função
imprimir_triangulo(n)