a = 'A'
b = 'B'
c = 1.1
d = '123'
string = 'a={0} a={0} a={0} b={1} c={2:.2f} d={3}'
formato = string.format(a, b, c, '123')

print(formato)

"""
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
"""