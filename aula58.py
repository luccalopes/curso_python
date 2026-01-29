x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        #print(f'Total: {total}')
        total += numero
        #print(numero, total)
    return total

soma1 = soma(1, 2, 3, 4, 5, 6)
print(soma1)