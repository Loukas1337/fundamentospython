# Criando uma lista dos sários
salarios = [200, 250, 390, 490, 590, 690, 790, 890, 990, 1000, 2000, 3000]

# Delimitando quantas faixas salariais são possíveis
contagem_faixa_salarial = [0] * 9

# Criando a leitura dos valores e determinando seus indices
for salario in salarios:
  indice = salario // 100 -2
  indice_maximo = len(contagem_faixa_salarial) - 1
  indice = min (indice, indice_maximo)
  contagem_faixa_salarial [indice]+=1

print(contagem_faixa_salarial)