# Criando um armazenamento para as letras que serão informadas pelo usuário
lista = []
consoantes = []

# Criando um armazenamento para dizer o que é vogal
vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(10):
  c = input(f'Digite o caracter {i+1}: ').lower() # Converter para minúsculo para facilitar a comparação
  lista.append(c)
  if c.isalpha() and c not in vogais: # Descobrindo se o caracter fornecido pelo usuário é uma letra, se sim, saber se é uma vogal
   consoantes.append(c)

print(f'Os caracteres são: {lista}')

print(f'Foram lidas {len(consoantes)} consoantes.')

print(f'As consoantes são: {consoantes}.')