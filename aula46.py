"""
Docstring for aula46
for in com listas
"""
# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('Tatiana')
# # for indice, nome in enumerate(lista):
# #     print(f'{indice}, {nome}')

# nome1, nome2, nome3, nome4 = lista

# print(nome2)

# _, _, nome, *resto =['Maria ', 'Helena ', 'Luiz']
# print(nome, resto)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Tatiana ')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])