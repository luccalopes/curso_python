def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'Lucca')
)
print(
    executa(saudacao, 'Boa noite', 'Lucca')
)
"""
High-order Functions e First-Class Functions
Academicamente, os termos Higher-Order Functions e First Class Functions tem significados diferentes

Higher Order Functions -> Funções que podem receber e/ou retornar outras funções

First Class Functions -> Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc)

"""