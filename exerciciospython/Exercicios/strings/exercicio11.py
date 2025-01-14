# Cód Renzo

# Cria uma variável para armazenar a palavra que precisa ser acertada
palavra = 'Devpro'.upper()


print('Jogo da forca')
print('Descubra a palavra')


# "Mostrando" a palavra que precisa ser acertada
print('A palavra é: ', end='')
for letra in palavra:
  print('_ ' , end='')


conjunto_letras_palavra = set(palavra) # Cria um conjunto com as letras da palavra
conjunto_letras_digitadas = set() # Cria um conjunto vazio para armazenar as letras digitadas pelo usuário
erros = 0 # Cria uma variável para armazenar o número de erros do usuário


while (not conjunto_letras_palavra.issubset(conjunto_letras_digitadas)) and erros < 7: # Verifica se o conjunto de letras da palavra está contido no conjunto de letras digitadas
  print()
  print()
  letra_digitada = input('Digite uma letra: ').upper()
  conjunto_letras_digitadas.add(letra_digitada) # Adiciona a letra digitada ao conjunto de letras digitadas
  if letra_digitada in conjunto_letras_palavra: # Verifica se a letra digitada está no conjunto de letras da palavra
    print('A palavra é: ', end='') # Mostra a palavra com as letras acertadas
    for letra in palavra:
      if letra in conjunto_letras_digitadas:
        print(f'{letra} ', end='')
      else:
        print('_ ', end='')
  else:
    erros += 1 # Soma os erros na variável
    print(f'-> Erro. {erros} de 6. Tente de novo.')


print()
print('Letras já digitadas: ', conjunto_letras_digitadas)


if erros < 7:
  print('Parabéns! Você ganhou!')
else:
  print('F! Você perdeu...')