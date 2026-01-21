"""
imprecisão de numeros de ponto flutuante em python
double-precision floating-point format IEEE 754
"""
import decimal

numero1 = decimal.Decimal('0.1')
numero2 = decimal.Decimal('0.7')
numero3 = numero1 + numero2

print(numero3)
print(f'{numero3:.2f}')
print(round(numero3, 3)) # retorna o número float formatado, primeiro argumento num segundo argumento casas decimais