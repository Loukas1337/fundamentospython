# Definindo a função para percorrer quantas vezes forem necessárias
def imprimir_padrao(n):
    for i in range(1, n + 1): # Percorre de 1 até n, imprimindo cada valor de i repetido i vezes.
        print((str(i) + " ") * i) # str(i) + " " Converte o número i para uma string e adiciona um espaço depois. (str(i) + " ") * i repete a string com o número i seguido de espaço, i vezes

# Solicita ao usuário o valor de n
try:
    n = int(input("Informe um valor inteiro para n: "))
    if n > 0:
        imprimir_padrao(n)
    else:
        print("Por favor, insira um número inteiro positivo.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")


#------------------------------------------------------------------------


def imprimir_triangulo_de_numeros(n: int): # Parâmetro n, um número inteiro que determina o número de linhas do triângulo
  for i in range(1, n + 1): # Ele percorre de 1 até n. A cada iteração, o valor de i define qual número será impresso e quantas vezes
    for _ in range(i): # Para cada linha, o valor de i é impresso i vezes
      print(i, end= '  ') # O uso do end=' ' garante que os números sejam impressos na mesma linha, separados por dois espaços
    print('') # Após cada linha, esse comando imprime uma nova linha, para separar os blocos de números


print('Triângulo com 1')
imprimir_triangulo_de_numeros(1)
print('Triângulo com 2')
imprimir_triangulo_de_numeros(2)
print('Triângulo com 3')
imprimir_triangulo_de_numeros(3)