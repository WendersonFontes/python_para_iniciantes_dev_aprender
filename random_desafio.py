from time import sleep
import random
moeda = ['Cara', 'Coroa']

print('Vamos jogar a moeda para o alto')

sleep(3)
moeda_resultante = random.choice(moeda)
print(f'A moeda resultante é {moeda_resultante}')

