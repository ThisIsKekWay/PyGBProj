from fractions import Fraction as F


def fraction(user_number_1, user_number_2, operation):
    user_number_1 = F(user_number_1).limit_denominator(10)
    user_number_2 = F(user_number_2).limit_denominator(10)
    if operation in ('+', '-', '*', '/'):
        if operation == '+':
            return str(user_number_1 + user_number_2)
        elif operation == '-':
            return str(user_number_1 - user_number_2)
        elif operation == '*':
            return str(user_number_1 * user_number_2)
        elif operation == '/':
            return str(user_number_1 / user_number_2)
