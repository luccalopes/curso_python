import re
import random
import sys

#sys.exit()
# entry = input('CPF: ')
# nine_digits = re.sub(r'[^0-9]', '', entry)
for _ in range(100):
    nine_digits = ''
    for i in range(9):
        nine_digits += str(random.randint(0, 9))

    countdown_timer_1 = 10

    digit1_result = 0
    for digit_1 in nine_digits:
        digit1_result += int(digit_1) * countdown_timer_1
        countdown_timer_1 -= 1 
    digit_1 = (digit1_result * 10) % 11
    digit_1 = digit_1 if digit_1 <= 9 else 0
    #print(digito_1)

    ten_digits = nine_digits + str(digit_1)
    countdown_timer_2 = 11

    digit2_result = 0
    for digit_2 in ten_digits:
        digit2_result += int(digit_2) * countdown_timer_2
        countdown_timer_2 -= 1
    digit_2 = (digit2_result * 10) % 11
    digit_2 = digit_2 if digit_2 <= 9 else 0
    #print(digito_2)

    new_cpf = f'{nine_digits}{digit_1}{digit_2}'

    print(new_cpf)