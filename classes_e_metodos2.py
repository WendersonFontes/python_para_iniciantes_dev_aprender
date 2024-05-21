class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    def ligar(self):
        print('Estou ligando')

    def desligar(self):
        print('Estou desligando')

    def exibir_info_computador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Asus', '16gb', 'Nvidia')
computador1.ligar()
computador1.desligar()
computador1.exibir_info_computador()
