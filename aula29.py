"""
introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao executar
"""

numero_str = input('Vou dobrar o numero que vc digitar ')

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    numero_dobrado = (numero_float) * 2
    print(f'O dobro do número {numero_str} é {numero_dobrado}')

except:
    print('Isso não é um número')

# if numero_str.isdigit():     
#     numero_float = float(numero_str)
#     numero_dobrado = (numero_float) * 2
#     print(f'O dobro do número {numero_str} é {numero_dobrado}')
# else:
#     print('Isso não é um número')