
while True:
    try:
        nota = int(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        else:
            print("Valor inválido. A nota deve ser entre 0 a 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")