
"""
métodos uteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com as chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave específica (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""
p1 = {
    'nome': 'Lucca',
    'sobrenome': 'Lopes',
}

# print(p1['nome'])
# print(p1.get('nome', 'None'))
# nome = p1.pop('nome')
# print(nome)
# print(p1)
# nome = p1.popitem()
# print(nome)
# print(p1)

# p1.update({
#     'nome': 'Bianca',
#     'sobrenome': 'Neme',
#     'idade': 28,
# })
tupla = (('Nome', 'novo valor'), ('idade', 30))
lista = [['Nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)



# import copy
# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }

# d2 = copy.deepcopy(d1)
# d2['l1'][1] = 99999

# d2['c1'] = 1000
# print(d1)
# print(d2)