'''
    Crie um array 5x5 com a sequência de números pares entre 0...50 (incluso) e faça as seguintes
    operações:
        1. Soma das linhas
        2. Soma das colunas
        3. Média dos elementos da última linha
        4. Média dos elementos da última coluna
'''

import numpy as np

numeros = []
for i in range(0, 50):

    if (i % 2) == 0:
        numeros.append(i)

# DataSet, nunca altera
dataSet = np.array(numeros).reshape((5,5))

somaLinhas = dataSet.sum(axis=1) # Lista a soma de cada linha
somaLinhas = somaLinhas.sum() # Soma tudo

somaColunas = dataSet.sum(axis=0) # Lista a soma de cada coluna
somaColunas = somaColunas.sum() # Soma tudo

mediaElementosLinha = int(np.median(dataSet[-1]))
temp = []

totalColunas = len(dataSet)
for i in range(0, totalColunas):
    temp.append(dataSet[i][totalColunas - 1])

mediaElementosColuna = int(np.median(temp))

print("1. Soma das linhas:", somaLinhas)
print("2. Soma das colunas:", somaColunas)
print("3. Média dos elementos da última linha:", mediaElementosLinha)
print("4. Média dos elementos da última coluna:", mediaElementosColuna)

