
# Criando a função para calcular o valor do produto com imposto
def somaimposto(taxaimposto, custo):
  valor_com_imposto = custo + (custo * (taxaimposto / 100))
  return valor_com_imposto

# Solicitando para o usuário a taxa e o custo do produto
taxa = float(input('Digite o valor da taxa (em %): '))
custo = float(input('Digite o custo do produto: '))

# Calculando o valor final
valorfinal = somaimposto(taxa, custo)


# Retornando ao usuário
print(f'O custo do produto é {custo}. Já a sua taxa é de {taxa}. O valor final fica {valorfinal}')