"""
operadores lógicos
and (e) or (ou) not(não)
and - todas as condições precisam ser verdadeiras
se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor são considerados falsy
"""
"""
entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
"""

# avaliação de curto circuito
#print(True and False and True)
#print(True and 0 and True)

if 1 and 1:
    print(True and 1 and False)