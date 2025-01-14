# Função que converte o horário de 24 horas para 12 horas
def converteHora(hora24, minuto):
    # Define A.M. ou P.M. dependendo da hora
    if hora24 == 0:
        hora12 = 12
        periodo = 'A'
    elif 1 <= hora24 < 12:
        hora12 = hora24
        periodo = 'A'
    elif hora24 == 12:
        hora12 = 12
        periodo = 'P'
    else:
        hora12 = hora24 - 12 # Converte qualquer hora no formato de 24 horas que esteja entre 13 e 23 em seu equivalente no formato de 12 horas
        periodo = 'P'

    return hora12, minuto, periodo


# Função para exibir a hora no formato 12 horas
def exibeHora(hora12, minuto, periodo):
    periodo_ext = 'A.M.' if periodo == 'A' else 'P.M.' # Determina se o horário é A.M. ou P.M., com tamanho_do_lado no valor de periodo, de acordo com a determinação da função
    print(f"{hora12}:{minuto:02d} {periodo_ext}") # Formatando os minutos como número inteiro (d de decimal), com 2 digitos.


# Função principal que permite repetir a conversão
def programaConversao():
    while True:
        # Entrada de dados
        hora24 = int(input("Digite a hora no formato 24 horas (0 a 23): "))
        minuto = int(input("Digite os minutos (0 a 59): "))

        # Converte e exibe a hora
        hora12, minuto, periodo = converteHora(hora24, minuto)
        exibeHora(hora12, minuto, periodo)

        # Pergunta se o usuário deseja repetir
        repetir = input("Deseja converter outro horário? (s/n): ")
        if repetir.lower() != 's':
            print("Encerrando o programa...")
            break

#Executar
programaConversao()