import math
while True:
    numero_1 = input('digite um número: ')
    numero_2 = input('digite outro número: ')
    operador = input('digite o operador: ( + - / *%//**) ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        soma = num_1_float + num_2_float
        subtracao = num_1_float - num_2_float
        multiplicacao = num_1_float * num_2_float
        divisao = num_1_float / num_2_float
        divisao_inteira = num_1_float // num_2_float
        modulo_resto = num_1_float % num_2_float
        exponenciacao = num_1_float ** num_2_float
        numeros_validos = True
    except:
        numeros_validos = None

        if numeros_validos is None:
            print('Um dos números digitados é inválido.')
            continue

    operadores_permitidos = '+-/*%//**'

    if operador not in operadores_permitidos:
        print('o operador é inválido. ')
        continue

    if len(operador) > 2:
        print('digite apenas um operador. ')
        continue

    print('Realizando a conta, confira o resultado abaixo.')

    if operador == '+':
        #soma = num_1_float + num_2_float
        print(soma)
    
    elif operador == '-':
        #subtracao = num_1_float - num_2_float
        print(subtracao)

    elif operador == '*':
        #multiplicacao = num_1_float * num_2_float
        print(multiplicacao)

    elif operador == '/':
        #divisao = num_1_float / num_2_float
        print(divisao)

    elif operador == '//':
        #divisao = num_1_float / num_2_float
        print(divisao_inteira)

    elif operador == '%':
        #divisao = num_1_float / num_2_float
        print(modulo_resto)

    elif operador == '**':
        #divisao = num_1_float / num_2_float
        print(exponenciacao)

    else:
        print('nunca deveria chegar aqui')

    sair = input('quer sair? [s]air ').lower().startswith('s')

    if sair:
        print('você saiu')
        break


