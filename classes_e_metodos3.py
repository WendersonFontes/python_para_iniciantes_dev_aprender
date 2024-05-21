class Carro:
    def __init__(self, acelerar, direita, esquerda, parar):
        self.acelerar = acelerar
        self.direita = direita
        self.esquerda = esquerda
        self.parar = parar

    def acelerou(self):
        print('Estou acelerando')

    def virou_direita(self):
        print('Estou virando a direita')

    def virou_esquerda(self):
        print('Estou virando a esquerda')

    def parou(self):
        print('Estou parando')

    def historico_deslocamento(self):
        print(f'O carro {self.acelerar}, {self.direita}, {self.esquerda}, e finalmente {self.parar}')    

meu_carro = Carro('Acelerou', 'Virou a direita', 'Virou a esquerda', 'Parou')

meu_carro.acelerou()
meu_carro.virou_direita()
meu_carro.virou_esquerda()
meu_carro.parou()
print('Histórico de deslocamento do veículo: ')
meu_carro.historico_deslocamento()