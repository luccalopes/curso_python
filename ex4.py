name = input('Digite o seu primeiro nome: ')
tamanho_nome = len(name)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é muito curto.')

    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')

    else:
        print('Seu nome é muito grande.')

else:
    print('Digite mais de uma letra')