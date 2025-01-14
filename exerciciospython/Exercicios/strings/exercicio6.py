# Dicionário com os meses do ano por extenso
meses = {
    "01": "janeiro", "02": "fevereiro", "03": "março",
    "04": "abril", "05": "maio", "06": "junho",
    "07": "julho", "08": "agosto", "09": "setembro",
    "10": "outubro", "11": "novembro", "12": "dezembro"
}


# Solicita a data de nascimento do usuário
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")


# Divide a data de entrada pelo usuáiro em dia, mês e ano
dia, mes, ano = data.split('/') # Quebra a string - dada pelo usuário - onde encontra barras (/) e retorna uma lista com três elementos: [dia, mês, ano].


# Exibe a data por extenso
if mes in meses:
    print(f"Você nasceu em {dia} de {meses[mes]} de {ano}.")
else:
    print("Data inválida! Por favor, insira no formato correto.")