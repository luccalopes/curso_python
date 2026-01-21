"""
Docstring for aula36
iterando strings com while
"""

nome = 'Lucca Lopes'
tamanho_nome = len(nome)
print(f'{nome}, {tamanho_nome}')

indice = 0
novo_nome = ''
while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

