class Bola: # Três atributos: Cor, circunferencia e material
    def __init__(self, cor, circunferencia, material): # Tudo que está dentro dos parenteses são chamados de parâmetros
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):  # Permite alterar a cor da bola
        self.cor = nova_cor

    def mostra_cor(self):  # Retorna a cor atual da bola
        return self.cor


# Exemplo de uso:
bola = Bola("Verde", 70, "Couro") # Bola é um objeto (nome técnico)

# Mostrando a cor atual
print(bola.mostra_cor())  # Saída Azul


# Trocando a cor
bola.troca_cor("Laranja")


# Mostrando a nova cor
print(bola.mostra_cor())  # Saída Vermelho