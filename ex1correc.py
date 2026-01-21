username = input('Digite o seu nome: ')
userage = input('Digite a sua idade: ')

if username and userage:
    print(f'Seu nome é {username}')
    print(f'Seu nome invertido é {username[::-1]}')
    
    if ' ' in username:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')

    print(f'Seu nome tem {len(username)} letras.')
    print(f'A primeira letra do seu nome é "{username[0]}".')
    print(f'A última letra do seu nome é "{username[-1]}".')

else:
    print('Preencha os campos obrigatórios.')