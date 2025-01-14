def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.

    Parâmetros:
    - numero: O número para o qual o fatorial será calculado.
    - show: (opcional) Se True, mostra o processo de cálculo na tela.

    Retorna:
    - O valor do fatorial de num.
    """
    resultado = 1 # Garantir que a primeira multiplicação seja válida e que o fatorial seja calculado corretamente
    for i in range(numero, 0, -1):
        resultado *= i # Pega o valor atual de resultado, multiplica pelo valor de i e armazena o novo valor em resultado. Acumula o produto dos números sucessivamente. Caso não houvesse esse código, não seria possível acumular o resultado e multiplicar pelo próximo número
        if show: # O parâmetro show é opcional (o padrão indicado na função é False) e indica se o processo de cálculo deve ser mostrado
          print(i, end=' x ' if i > 1
        else ' = ')
    return resultado

# Retornando a resolução para o usuário
print(fatorial(5)) # Apenas exibe o resultado
print(fatorial(5, show=True)) # Exibe o processo e o resultado