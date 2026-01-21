hours_str = input('Que horas são? ')

try:
    hours_float = float(hours_str)
    if hours_float <= 23.59 and hours_float >= 19.00:
        print(f'Boa noite. Agora são {hours_str} horas.')
    
    elif hours_float <= 18.59 and hours_float >=12.00:
        print(f'Boa tarde. Agora são {hours_str} horas.')
    
    elif hours_float <= 11.59 and hours_float >=00.00:
        print(f'Bom dia. Agora são {hours_str} horas.')
    else:
        print('hora inválida')

except:
    print('Digite a hora em números.')