'''
    Crie um array 5x5 com a sequência 1...25 (incluso) e faça a soma dos elementos da diagonal.
'''

import numpy as np


a = np.array([i for i in range(1,26)]).reshape((5,5))

elementosDiagonal = list(np.diag(a)) # Lista dos elementos Diagonal

somaElementos = np.sum(elementosDiagonal) # Soma dos elementos

print("Elementos Original:", a)
print("Elementos Diagonal:", elementosDiagonal)
print("A Soma dos elementos Diagonal é:",somaElementos)