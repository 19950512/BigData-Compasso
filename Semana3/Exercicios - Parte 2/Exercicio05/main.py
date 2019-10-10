'''
    Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
    Utilize um exemplo para testar sua função.
'''

def novaLista(lista):
    return list(set(lista))

' Data set'
lista = [0, 1, 0, 1, 2, 3, 4, 4, 8, 12, 3, 14, 13]

novaLista = novaLista(lista)

' Exemplo de uso'
print("Lista:", lista)
print("Nova Lista:", novaLista)