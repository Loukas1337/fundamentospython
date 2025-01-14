# Crie um programa que tenho uma tupla totalmente preenchido com uma contagem por extenso. de zero oté vinta. Seu programa deverá ler um número pelo Eeclado (entre 0 e 20) ae mostrá-lo por extenso.

c = ("zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
  p = int(input('Digite um número de 0 a 20: '))
  if 0 <= p <= 20:
    break
print(f'O número digitado foi: {c[p]}')