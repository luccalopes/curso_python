string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    ['Maria', 'Elaine',],
    ['Helena',],
    ['Luiz', 'João', 'Eduardo',],
]

# a, b, c, *_, u = lista
# print(a, u)

# for nome in lista:
#     print(nome, end=' ')

print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')