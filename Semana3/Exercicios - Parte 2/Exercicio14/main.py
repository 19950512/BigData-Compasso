'''
    Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula
    abaixo:
    Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
'''

import random as rand
import numpy as np

# amostra aleatoriamente 50 números do intervalo 0...500
random_list = rand.sample(range(500), 50)

random_list = np.sort(random_list)

maximo = np.max(random_list)
medio = int(np.around(np.median(random_list) + 0.5)) #Arredonda para cima, converte para inteiro'
minimo = np.min(random_list)

print("Números:",random_list)
print("Máximo:",maximo)
print("Médio:",medio)
print("Mínimo:",minimo)
