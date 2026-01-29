def multip(*args):
    total = 1
    for i in args:
        total *= i
    print(total)

def par_impar(numero):
    multplo_de_2 = numero % 2 == 0
    
    if multplo_de_2:
        return f'{numero} é par'
    return f'{numero} é impar'


    
#multip(5, 0)
print(par_impar(2))