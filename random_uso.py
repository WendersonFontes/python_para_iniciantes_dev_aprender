# simular a opção de  jogar uma moeda e resultar em cara ou coroa 
# fazer um sorteio entre 300 nomes em uma lista de nomes
# escolher aleatoriamente um numero de 10-100
# escolher carta aleatoria dentro de um baralho
# gerar nomes de usuário
# gerar senhas

import random

print(random.random()) #valor 0.0 até 1.0
print(random.uniform(4,10)) # valor decimal de mínimo ao máximo
print(random.randint(12, 55)) # valor de mínimo ao máximo

cores = ['verde', 'vermelho', 'azul']
print(random.choice(cores)) #escolher uma opções dentro de uma fonte

cartas_de_um_baralho = ['carta1' , 'carta2', 'carta3',  'carta4', 'carta5']
random.shuffle(cartas_de_um_baralho)
print(cartas_de_um_baralho)