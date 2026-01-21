primeiro_valor = int(input('digite um valor: '))
segundo_valor = int(input('digite outro valor: '))

if primeiro_valor > segundo_valor:
    print(f'o primeiro valor "{primeiro_valor}" é maior do que o segundo valor "{segundo_valor}"')
elif segundo_valor > primeiro_valor:
    print(f'o segundo valor "{segundo_valor}" é maior do que o primeiro valor "{primeiro_valor}"')
else:
    print('ambos os valores são iguais')