"""
dicionarios em Python (tipo dict)
dicionários são estruturas de dados do tipo par de "chave" e "valor"
chaves são consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis, como: str, int, float, bool, tuple, etc.
o valor pode ser de qualquer tipo, incluindo outro dicionário.
usamos as chaves - {} - ou a classe dict para criar dicionários.
imutáveis: str, float, int, bool, tuple
mutável: dict, list

pessoa = {
    'nome': 'Lucca',
    'sobrenome: 'Lopes',
    'idade': 29
    'altura': 1.7,
    'endereços': [
        {'rua': 'rua tal', 'número': 0},
        {'rua': 'outra rua', 'número': 1},
    ]
}
print(pessoa, type(pessoa))
"""
pessoa = {
    'nome': 'Lucca',
    'sobrenome': 'Lopes',
    'idade': 29,
    'altura': 1.7,
    'enderecos': [
        {'rua': 'rua Guatemala', 'numero': 102},
        {'rua': 'rua Geraldo Beting', 'numero': 300}
    ]
}
#print(pessoa, type(pessoa))
print(pessoa['nome'], pessoa['sobrenome'], pessoa['enderecos'])

for chave in pessoa:
    print(chave, pessoa[chave])