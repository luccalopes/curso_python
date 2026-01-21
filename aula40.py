# senha_salva = '123456'
# senha_digitada = ''

# repeticoes = 0

# while senha_salva != senha_digitada:

#     senha_digitada = input(f'Sua senha ({repeticoes} x): ')
#     repeticoes += 1

# print(repeticoes)
# print('aquele laço lá em cima pode ter repetições infinitas')

texto = 'Python'
novo_texto = ''

for letra in texto: # a variável é criada como parametro do for
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')