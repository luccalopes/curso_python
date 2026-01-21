numero_str = input('Digite um número inteiro: ')

try:
    print(numero_str)
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print(f'O número {numero_str} é par.')
    else:
        print(f'O número {numero_str} é impar.')

except:
    print('Isso não é um numero')