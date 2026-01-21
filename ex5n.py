import os
palavra_secreta = 'itaquaquecetuba'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Você acertou')
        print(f'A palavra era {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        letras_acertadas = ''
        tentativas = 0
        