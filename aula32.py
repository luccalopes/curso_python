"""
https://docs.python.org/3/library/stdtypes.html
imutáveis que vimos: int, float, str, bool
"""

string = 'lucca'
outra_string = f'{string[:2]}ABC {string[4:]}'
#string[3] = 'ABC'
capitalize = string.lower()

print(outra_string.capitalize())
print(capitalize)