# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite seu sexo, onde M para masculino, F para feminino e I para indefinido ').upper()
if sexo == 'M':
  print ('Sexo masculino')
elif sexo == 'F':
  print ('Sexo feminino')
elif sexo == 'I':
  print ('Sexo indefinido')
else:
  print ('sexo inválido')

print ('programa finalizado')