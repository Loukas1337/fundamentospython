lista = [1, 3, 7, 5, 0]
lista.append(8)
print(lista)
if 9 in lista:
  lista.remove(9)
else:
  print('Nao achei o numero na lista')
# lista.sort(reverse=True)
# lista.remove(1)
print(f'Essa lista possui {len(lista)} elementos')