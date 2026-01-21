"""
Iterável -> str, range, etc (___iter___)
iterador -> método que entrega um vlor por vez
next -> entrega o próximo valor
iter -> entrega o iterador
"""


# for + range

# texto = 'Lucca'
# numeros = range(0, 100, 8) # range -> start, stop, step (início, fim e passo)
# numeros = range(5, 10, 2)
# print(numeros)

# for numero in numeros:
#     print(numero)

texto = ('Lucca')
#iterador = iter(texto)

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)

#     except StopIteration:
#         break
    
for letra in texto:
    print(letra)
