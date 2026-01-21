"""
interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal(ABCDEF0123456789)
"""
nome = 'Lucca'
preco = 1000.95897643
# o operador % retorna os valores das interpolações
# usamos as letras seguidas das interpolações para retornar o valor desejado
# após fechar a string é necessário usar novamente o operador % seguido dos parâmetros (variáveis) entre parenteses
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexacecimal de %i é %04x' % (1500, 1500))