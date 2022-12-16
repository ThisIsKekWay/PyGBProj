from fractions import Fraction as F

def fraction(user_number_1, user_number_2, operation):
    user_number_1 = F(user_number_1).limit_denominator(10) # Переводим полученные значения в дроби и "округляем"
    user_number_2 = F(user_number_2).limit_denominator(10)
    if operation in ('+', '-', '*', '/'):                  #Тут все просто, возвращаем результат нужной операции , например в переменную, сразу в строку.
        if operation == '+':
            return user_number_1 + user_number_2
        elif operation == '-':
            return user_number_1 - user_number_2
        elif operation == '*':
            return user_number_1 * user_number_2
        elif operation == '/':
            return user_number_1/user_number_2
def checking(res):
    if res.numerator > res.denominator:
        while res.numerator > res.denominator:
            find_whole_part = (res.numerator // res.denominator)
            find_numerator = res.numerator % res.denominator
            push_itog = str(find_whole_part) + ' ' + str(find_numerator) + '/' + str(res.denominator)
            return push_itog
    else: return str(res)
    