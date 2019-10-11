'''
    Leia o arquivo actors.csv e faça os seguintes cálculos sobre o conjunto de dados:
    1. O ator/atriz com maior número de filmes e o respectivo número de filmes.
    2. A média do número de filmes.
    3. O ator/atriz com a maior média por filme.
    4. O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
'''


import csv
import numpy  as np

nomeArquivo = 'actors.csv'
with open(nomeArquivo, newline='') as arquivo:
    dataSet = list(csv.reader(arquivo))

autoresFilmes           = [] # Lista com um "novo" dataSet
numeroFilmes            = [] # Lista com todos os número Filmes
numeroFrequencia        = [] # Lista com todos os número Frequencia
numeroMediaFilmes       = [] # Lista com todas as médias de filme, somente número

for i in range(1, len(dataSet)):
    # nome do autor, número de filmes, media filmes, nome filme, bruto?
    autoresFilmes.append([dataSet[i][0], dataSet[i][2], dataSet[i][3], dataSet[i][4], dataSet[i][5]])

    # adiciona o número de filmes a lista numeroFilmes
    numeroFilmes.append(int(dataSet[i][2]))

    # adiciona o número Media de filmes a lista numeroMediaFilmes
    numeroMediaFilmes.append(float(dataSet[i][3]))

    # adiciona o número Frequencia/bruto ? a lista numeroFrequencia
    numeroFrequencia.append(float(dataSet[i][5]))


maiorNumeroFilmes   = np.max(numeroFilmes) # Busca o maior número
respostaDois        = int(np.median(numeroFilmes)) # Busca a media do número Filmes
respostaTres        = np.max(numeroMediaFilmes) # Busca o maior número da numeroMediaFilmes
respostaQuatro      = np.sort(numeroMediaFilmes)[:-5:-1] # Busca os 4 primeiros MAIORES numeros

respostaUm = ''
respostaTresSTR = ''
respostaQuatroSTR = []
for i in range(0, len(autoresFilmes)):

    if int(autoresFilmes[i][1]) == maiorNumeroFilmes:
        respostaUm = str(autoresFilmes[i][0]) + " - " + str(autoresFilmes[i][1])

    if float(autoresFilmes[i][2]) == respostaTres:
        respostaTresSTR = str(autoresFilmes[i][0]) + " - " + str(autoresFilmes[i][2])

for i in range(0, len(respostaQuatro)):
    for x in range(0, len(autoresFilmes)):
            print(respostaQuatro[i], autoresFilmes[x][3])


print("1. O ator/atriz com maior número de filmes e o respectivo número de filmes:" + respostaUm)
print("2. A média do número de filmes.:", respostaDois)
print("3. O ator/atriz com a maior média por filme.", respostaTresSTR)
print("4. O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.")
print(respostaQuatroSTR)
