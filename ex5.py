palavra_secreta = 'itaquaquecetuba' # palavra do game precisa estar fora do looping
letras_acertadas = '' # string vazia onde será salva as letras certas
while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas = 0

    if len(letra_digitada) > 1: # certifica de que o que foi digitado no input seja apenas um caractere
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta: # verifica se a letra digitada no input está na palavra secreta
        letras_acertadas += letra_digitada # salva a letra digitada certa na string vazia

    palavra_formada = '' # string vazia para receber as letras conforme vai acertando a palavra
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta # se a letra secreta estiver na palavra formada, a palavra formada recebe essa letra
        else:
            palavra_formada += '*' #senão as letras ficarão ocultas

    print(palavra_formada)
