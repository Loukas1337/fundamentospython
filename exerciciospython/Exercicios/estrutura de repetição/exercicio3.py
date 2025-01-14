# Nome maior que 3 caracteres

nome = str(input('Digite seu nome: '))
while (len(nome)) <= 3: #Len é uma função que retorna o numero de itens de um objeto.
  nome = str(input('Digite seu nome: '))


# Idade estar entre 0 e 150

idade = int(input('Digite sua idade: '))
while 0 < idade > 150:
  idade = int(input('Digite sua idade: '))

# Perguntando o salário

salario = float(input('Qual seu salário: '))
while salario <= 0:
  salario = float(input('Qual seu salário: '))

# Perguntando o sexo

sexo = str(input('Qual seu sexo? Onde "M" para masculino e "F" para feminino: ')).upper()
while sexo != "F" and sexo != "M":
  sexo = str(input('Qual seu sexo? Onde "M" para masculino e "F" para feminino: ')).upper()

# Perguntando o estado civil
estado_civil = str(input('Qual seu estado civil? Onde "s" para solteiro, "c" para casado, "v" para viuvo e "d" para divorciado: ')).lower()
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
  estado_civil = str(input('Qual seu estado civil? Onde "s" para solteiro, "c" para casado, "v" para viuvo e "d" para divorciado: ')).lower()
print('Finalizado.')