"""
listas em Python
tipo list - mutável
suporyta vários valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamento
métodos uteis: 
    append, insert, pop, del, clear, extend
Create Read Update Delete
"""

# ........... 01234
# .......... -54321
lista = [10, 20, 30, 40, 50, 60]
print(lista)
lista[2] = 300
print(lista)
del lista[1] # remove um item no indice da lista
print(lista)
lista.append(70) # adiciona um item ao final da lista
print(lista)
lista.pop() # remove o ultimo item da lista
print(lista)
del lista[-1]
print(lista)
# lista.clear() # limpa a lista
# print(lista)
lista.insert(3, [5, 'tô parando de fumar', True, False, 1.53]) # primeiro vai o indice e depois o valor
print(lista)
lista.insert(100, 3)
print(lista[-1])


