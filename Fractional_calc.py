from fractions import Fraction as F
global res


def fraction(user_number_1, user_number_2, operation):
    user_number_1 = F(user_number_1)
    user_number_2 = F(user_number_2)
    if operation in ('+', '-', '*', '/'):
        if operation == '+':
            res = user_number_1 + user_number_2
        elif operation == '-':
            res = user_number_1 - user_number_2
        elif operation == '*':
            res = user_number_1 * user_number_2
        elif operation == '/':
            res = user_number_1/user_number_2

    if res.numerator > res.denominator:
        while res.numerator > res.denominator:
            find_whole_part = (res.numerator // res.denominator)
            find_numerator = res.numerator % res.denominator
            push_itog = f'{res} = {find_whole_part} {find_numerator}/{res.denominator}'
            res = f'{user_number_1} {operation} {user_number_2} = {push_itog}'
            return res
    else:
        res = f'{user_number_1} {operation} {user_number_2} = {res}'
        return str(res)
    