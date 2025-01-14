
#Criando uma lista para receber os números colocados pelo usuário
notas = []

# Criando laço para solicitar o número
while True:
  entrada = (input('Digite um número ou -1 para encerrar: '))
  if entrada == '-1':
    break
  notas.append(float(entrada))

# Calculando o tamanho da lista
tamanho = len(notas)
print(f'Foram lidas {tamanho} notas')


# Convertendo todos os valores em string
print(','.join([str(nota) for nota in notas]))
notas.reverse()  # Valores na ordem inversa do que se foi informado

# Mostrando as notas
for nota in notas:
  print(nota)

# Calculando a soma dos números informados
soma = sum(notas)

print(f'soma das notas é: {soma}')

# Calculando a média dos números informados
media = soma / tamanho

print(f'A média das notas é: {media}')

# Mostrando números que são maiores que a média
print(', '.join([str(nota) for nota in notas if nota > media]))

# Mostrando números que são menores que 7
print('Notas abaixo de 7: ')
print(','.join([str(nota) for nota in notas if nota < 7]))


print('Programa encerrado.')



#--------------------------

# Outra forma de resolver

def main():
    notas = []  # Lista para armazenar as notas

# Leitura dos valores (notas)
    while True:
        nota = float(input("Informe uma nota (ou -1 para encerrar): "))
        if nota == -1:
            break
        notas.append(nota)

# 1. Mostrar a quantidade de valores lidos
    quantidade = len(notas)
    print(f"Quantidade de valores lidos: {quantidade}")

# 2. Exibir todos os valores na ordem em que foram informados, um ao lado do outro
    print("Valores na ordem informada:", " ".join(map(str, notas))) # Sem o map(), teria que manualmente converter cada número para string antes de usar o join(). Ele facilita essa conversão de maneira mais eficiente.

# 3. Exibir todos os valores na ordem inversa à que foram informados, um abaixo do outro
    print("\nValores na ordem inversa:")
    for nota in reversed(notas):
        print(nota)

# 4. Calcular e mostrar a soma dos valores
    soma = sum(notas)
    print(f"\nSoma dos valores: {soma}")

# 5. Calcular e mostrar a média dos valores
    if quantidade > 0:
        media = soma / quantidade
        print(f"Média dos valores: {media:.2f}")
    else:
        media = 0
        print("Média dos valores: 0 (Nenhuma nota foi inserida)")

# 6. Calcular e mostrar a quantidade de valores acima da média
    acima_da_media = len([nota for nota in notas if nota > media])
    print(f"Quantidade de valores acima da média: {acima_da_media}")

# 7. Calcular e mostrar a quantidade de valores abaixo de sete
    abaixo_de_sete = len([nota for nota in notas if nota < 7])
    print(f"Quantidade de valores abaixo de sete: {abaixo_de_sete}")

# 8. Encerrar o programa com uma mensagem
    print("\nPrograma encerrado. Até a próxima!")

if __name__ == "__main__":
    main()