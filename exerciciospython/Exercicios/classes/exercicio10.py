class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
        print(f"Nome do correntista alterado para: {self.nome_correntista}")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}") # O motivo do uso de :.2f é: Dois pontos inicia a especificação do formato, .2 indica que queremos duas casas decimais e f  significa "floating-point number" (número de ponto flutuante)
        else:
            print("Valor de depósito inválido!")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor de saque inválido!")

conta = ContaCorrente(1234, 'Lili', 3000)
conta.alterar_nome('Juju')
conta.deposito(100)
print(conta.saldo)
print(conta.nome_correntista)