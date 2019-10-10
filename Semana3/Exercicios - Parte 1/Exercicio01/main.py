'''
    Escreva um código Python que lê do teclado o nome e a idade de um usuário e imprime o ano
    em que o usuário completará 100 anos.

    Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem').
    Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações
    aritméticas.
'''

import os
from datetime import datetime
data = datetime.now()

def clear():

    ' Simples função para limpar o terminal'
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:
        ' Recupera o nome do usuário'
        nome = input("Qual é o seu nome? \n")

        if nome == "":
            print("Ops, Informe seu nome.")
            continue

        ' Limpa o terminal'
        clear()

        ' Recupera a Idade do usuário'
        idade = int(input("Qual a sua idade ? \n"))

        if idade < 1:
            print("Ops, Não podemos prever sua idade.")
            continue

        ' Limpa o terminal'
        clear()

        ' Pega a diferença da idade para a quantidade de anos que queremos verificar'
        diferenca = 100 - idade

        ' Calcula o ano atual + a diferença de idade em relação ao periodo de 100 Anos'
        calcula = int(data.year) + diferenca

        print(nome + ", você irá completar 100 anos em", calcula, ". Faltam", diferenca, "anos!")
        print('___________________________ \n\n')

    except:
        ' Limpa o terminal'
        clear()

        print("Ops, algo de errado não está certo.")

