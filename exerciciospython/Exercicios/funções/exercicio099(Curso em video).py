# Função maior que recebe vários parâmetros

def maior(*numeros):
    # Verifica se foram passados números
    if len(numeros) == 0:
        print("Nenhum número foi informado.")
    else:
        # Encontra o maior número
        maior_numero = max(numeros)

        # Exibe os números informados e o maior número
        print("Analisando os números:", numeros)
        print(f"O maior número informado foi: {maior_numero}")

# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(1, 3, 5)
maior(8, 3, 6, 9, 4, 10)
maior()