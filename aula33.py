"""
repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um código não tem fim
"""

# condicao = True

# while condicao:
#     nome = input('Qual é o seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break

# print(123)

# while contador <= 12:
#     print(contador)
#     contador = contador + 1
#     #print(contador)

# print('acabou')

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('não vou mostrar o 6')
        continue # o método continue faz o item ser ocultado

    if contador >= 10 and contador <=27:
        print(f'não vou mostrar o {contador}')
        continue

    print(contador)

    if contador == 40:
        print(contador)
        break

    #print(contador)

print('acabou')

