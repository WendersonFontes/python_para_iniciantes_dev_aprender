class Carro:
    def __init__(self, cor, modelo, preco):
        self.cor = cor
        self.modelo = modelo
        self.preco = preco
    def ligar_carro(self):
        print(f'Ligando o carro {self.modelo}')

mustang = Carro('Laranja', 'Mustang GT', '250000')
mustang.ligar_carro()