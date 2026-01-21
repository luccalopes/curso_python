"""
introduções às funções (def) em Python
funções são trechos de código usados para replicar determinada ação ao longo do código
elas podem receber valores para parâmetros (argumentos) e retornar um valor específico
por padrão, funções Python retornam None (nada)
"""
# def Print(a, b, c):
#     print(a, b, c)

# Print(1, 2, 3)

# def saudacao(nome='John Doe'):
#     print(f'Olá, {nome}!')

# saudacao('Lucca')
# saudacao()
def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)