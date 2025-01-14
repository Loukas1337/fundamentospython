while True:
  nome = str(input('Digite seu nome: '))
  senha = str(input('Digite sua senha: '))

  if senha == nome:
    print('A senha nao pode ser igual ao nome. Tente novamente.')

  else:
    print('Concluído')
    break