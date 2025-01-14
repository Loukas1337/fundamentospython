class TV:
    def __init__(self):
        self.canal = 1           # Canal inicial
        self.volume = 10          # Volume inicial
        self.max_canal = 100      # Canal máximo
        self.min_canal = 1        # Canal mínimo
        self.max_volume = 100     # Volume máximo
        self.min_volume = 0       # Volume mínimo

    def mudar_canal(self, novo_canal):
        if self.min_canal <= novo_canal <= self.max_canal:
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print(f"Canal inválido! Escolha um canal entre {self.min_canal} e {self.max_canal}.")

    def aumentar_volume(self):
        if self.volume < self.max_volume:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume máximo atingido!")

    def diminuir_volume(self):
        if self.volume > self.min_volume:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume mínimo atingido!")

# Exemplo de uso
tv = TV()
tv.mudar_canal(8)     # Mudar para o canal 5
# Caso queira aumentar ou diminuir o volume várias vezes de uma só vez, será necessário criar uma contagem com o for
for _ in range(15):   # Diminuindo o volume várias vezes
 tv.diminuir_volume()

tv.aumentar_volume()  # Aumentar o volume
tv.diminuir_volume()  # Diminuir o volume