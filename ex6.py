import os
lista_de_compras = []
while True:
    opcoes = input('O que você deseja fazer? [I]nserir [A]pagar [L]istar [S]sair do programa ')
    letras_permitidas = 'I' 'A' 'L' 'S'

    if opcoes not in letras_permitidas:
        print('Você digitou uma opção inválida. Digite uma das letras permitidas.')
        continue

    elif opcoes == 'I':
        os.system('cls')
        lista = input('Qual item você gostaria de adicionar? ')
        lista_de_compras.append(lista)
        continue

    elif opcoes == 'A':
        if lista_de_compras == []:
            print('Sua lista está vazia.')
            continue
        excluir = input('Qual item você gostaria de remover? ')
        try:
            os.system('cls')
            apagar = int(excluir)
            lista_de_compras.pop(apagar)
            print('Item excluído. ')
        
        except ValueError:
            print('Escolha um item válido dentro dos índices')
            
        except IndexError:
            print('Digite um índice válido')
            continue

    elif opcoes == 'L':
        os.system('cls')
        if lista_de_compras == []:
            print('Sua lista está vazia. ')
            continue
        for indice, nome in enumerate(lista_de_compras):
            print(indice, nome)
            continue
        
    else:
        os.system('cls')
        print('Você saiu do programa.')
        break