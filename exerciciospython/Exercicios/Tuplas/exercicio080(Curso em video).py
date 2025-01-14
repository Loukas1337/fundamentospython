lista = []
for c in range(0, 5):
  n = int(input('Digite um número: '))
  if c == 0 or n > lista[-1]:
    lista.append(n)
    print('Adicionado ao final da lista')
  else:
    pos = 0
    while pos < len(lista):
      if n <= lista[pos]:
        lista.insert(pos, n)
        print(f'Adicionado na posição {pos} da lista')
        break
      pos += 1

print(f'A lista em ordem correta é: {lista}')

#---------- Outra forma de fazer (mais fácil)

# Com esse import, nos é fornecido funções para trabalhar com listas ordenadas, inserir e buscar elementos de forma eficiente. Ele é útil quando você deseja manter uma lista sempre ordenada à medida que você insere novos elementos, sem precisar reordená-la manualmente após cada inserção.
import bisect

# Criando a lista para receber os números
numeros = []
# Criando o laço para realizar a coleta dos números
for i in range(5):
    n = int(input('Digite um número: '))
    bisect.insort(numeros, n) # A função insort() do módulo bisect insere o número na posição correta dentro da lista ordenada.
    print(f'Número {n} incluído na posição {numeros.index(n)}') # Após a inserção, a posição do número recém-adicionado é mostrada.
print(f'Número contados: {numeros}')