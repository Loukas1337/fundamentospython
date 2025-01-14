#Cod Renzo

def validar(ip:str) -> bool:
  numeros = ip.split('.') # Divide o endereço IP em partes separadas pelos pontos, ex: ['192', '168', '0', '1']

  if len(numeros) != 4: # Criando um laço para saber se o tamanho do ip é diferente de 4, se sim, ele é considerado inválido (visto que, um IP sempre possui 4 números)
    return False

  for n in numeros:
    if not (0 <= int (n) <= 255): # Verifica se é um número e está no intervalo permitido
      return False
  return True # Retorna True apenas se todos os números forem válidos

# Criando listas para receber os ips
ips_validos = []
ips_invalidos = []

# Lê o arquivo de entrada
with open('sample_data/ips.txt', 'r') as arquivo: # Comando para ler um arquivo. Além disso, ele estará aberto dentro da identação do with
  for linha in arquivo:
    ip = linha.strip() # Remover espaços extras ou quebras de linha que possam causar erros na validação do IP
    if validar(ip):
      ips_validos.append(ip)
    else:
      ips_invalidos.append(ip)

# Abre o arquivo secundário (arquivo de saída) e escreve uma linha
with open('sample_data/ips_saida.txt', 'w') as arquivo:
  arquivo.writelines ('[Endereços válidos:]\n')

# Escreve os ips válidos no arquivo de saída (segundo arquivo)
  for ip in ips_validos:
    arquivo.writelines (f'{ip}\n')

#Dá espaçamento no arquivo de saída e escreve uma linha ([Endereços inválidos:])
  arquivo.writelines ('\n')
  arquivo.writelines ('\n')
  arquivo.writelines ('[Endereços inválidos:]\n')

# Escreve os ips inválidos no arquivo de saída (segundo arquivo)
  for ip in ips_invalidos:
    arquivo.writelines (f'{ip}\n')