'''
    Escreva uma função que recebe um número variável de parâmetros não nomeados e um número
    variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
'''

def ParametroNaoNomeados(*args):
    print(args)

def ParametroNomeados(**kwargs):
    print(kwargs)


print("Função com Parâmetro não nomeados")
ParametroNaoNomeados('Lorem', 'Ipsum', 2019, [1, 2, 3])

print("\n")

print("Função com Parâmetro nomeados")
ParametroNomeados(primeiro = "Lorem", segundo = "Ipsum", terceiro = 2019, quarto = [1, 2, 3])