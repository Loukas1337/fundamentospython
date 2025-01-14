notas = []

for i in range(4):
  n = float(input('Digite uma nota: '))
  notas.append(n)
print(f'As notas são: {notas}')

media = sum(notas) / 4

print(f'A média é das notas é {media}')