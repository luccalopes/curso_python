lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # o método já concatena as duas strings, não sendo possível jogar dentro de uma nova variável
print(lista_c)
print(lista_a)
lista_a.reverse()
print(lista_a)