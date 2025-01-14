valores = []
listap = []
listai = []

while True:
  n = int(input('Digite um número: '))
  if n not in valores:
    valores.append(n)
    print('Valor inserido com sucesso!')
  r = str(input('Quer continuar? S/N '))
  if r in 'Nn':
    break


for i, n in enumerate(valores):
  if n % 2 == 0:
    listap.append(n)
  elif n % 2 == 1:
    listai.append(n)


print(f'A primeira lista que contém todos os valores: {valores}')
print(f'A segunda lista dos números pares: {listap}')
print(f'A terceira lista dos números ímpares: {listai}')