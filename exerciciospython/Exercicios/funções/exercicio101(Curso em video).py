# Solicitando o ano de nascimento para o usuário
nascimento = int(input('Em que ano você nasceu? '))

# Convertendo o ano em idade
nascimento1 = 2024 - nascimento

# Criando a função para determinar se o voto é obrigatório, opcional ou negado
def voto(nascimento1):
  if 16 <= nascimento1 < 18:
    print('Opcional')
  elif nascimento1 < 16:
    print('Negado')
  elif 18 <= nascimento1 == 70:
    print('obrigatório')
  else:
    print('Opcional')


#Chamando a função
voto(nascimento1)