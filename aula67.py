"""
Sets - conjuntos em Python (tipo set)
conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém só aceitam tipos imutáveis como valores
como criar um set - set(iteravel) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados de iteráveis
Seus valores são sempre únicos
não aceitam valores mutáveis
não tem indexes
não garantem ordem
são iteráveis (for, in, not in)

métodos úteis:
add, update, clear, discard

operadores úteis:
união | (union) - une
intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes em ambos
diferença simétrica ^ itens que não estão em ambos
para inserir uma string sem comprometer a ordem, deve-se colocar a string como um iterável ()
"""

#s1 = {1, 2, 3, 3, 3, 3, 4, 1}
# l1 = [1, 2, 3, 3, 3, 3, 4, 1]
# s1 = set(l1)
# l2 = list(s1)

# print(l1)
# print(s1)
# print(l2)

s1 = set()
s1.add(('Lucca'))
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
print(s1)
s1.discard('Lucca')
print(s1)
s1.add('Lucca')
print(s1)
print()

# s1.clear()
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s2 - s1
print(s3)