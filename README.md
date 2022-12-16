# PyGBProj

Блок комплексных чисел: Евгений

Блок дробей: Егор

Логирование: Кирилл

~~Программа минимум: реализовать минимальный функционал (простейшие операции, логирование)~~

## Описание

Программа состоит из нескольких модулей.

### Модуль логирования ```logging```

```buildoutcfg
from datetime import datetime as dt

def logging_to_file(arithmetic):
    path = "log.csv"
    time_sign = dt.now().strftime('%D %H:%M')
    f = open('log.csv', "a")
    f.write(f'{time_sign}--> {arithmetic}\n')
    f.close() 
```

Модуль реализован функцией ```logging_to_file``` принимающей в качестве аргумента строку, содержащую готовое выражение.

Импортирована библиотека ```datetime``` для отображения времени.

Функция записывает данные в файл ```log.csv```

### Модуль обработки и расчета комплексных чисел ```Complex_calc```

```buildoutcfg
def arithmetic(a, b, symbol_operator):
    complex1 = complex(a[0], a[1])
    complex2 = complex(b[0], b[1])
    operation = {'+': lambda x, y: x+y,
                 '-': lambda x, y: x-y,
                 '*': lambda x, y: x*y,
                 '/': lambda x, y: x/y}

    res = f'{complex1} {symbol_operator} {complex2} = {operation[symbol_operator](complex1, complex2)}'
    if str(operation[symbol_operator](complex1, complex2))[3] == '0':
        return res[:-4:] + ')'
    else:
        return res
```
Модуль реализован функцией ```arithmetic``` принимающей в качестве аргументов два списка и одну строковую переменную.

Списки являются введенными пользователем значениями действительных и мнимых частей комплексных чисел.

Строковая переменная содержит действие, совершаемое с этими числами.

Функция передает данные в главный модуль ```main``` для дальнейшего логирования.

### Модуль обработки и расчета натуральных дробей ```Fractional_calc```
```buildoutcfg
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
```

Модуль реализован функцией ```fraction``` принимающей в качестве аргументов три строковых переменных.

Строки являются введенными пользователем значениями числителей и знаменателей дробей, а также выбранное пользователем арифметическое действие.

Функция передает данные в главный модуль ```main``` для дальнейшего логирования с возможностью выделения целой части итоговой дроби

### Модуль управления ```main```

```buildoutcfg
from Complex_calc import arithmetic
from Fractional_calc import fraction
from logging import logging_to_file
words1 = {0: 'Действительную часть', 1: 'Мнимую часть'}
words2 = {0: 'Числитель', 1: 'Знаменатель'}
num1 = list()


def validation(a):
    try:
        int(a)
        return True
    except:
        print('Введены неверные данные\n')
        return False


print('Калькулятор запущен...\n'
      'Выберите тип вычисления:\n'
      '1) Операции с комплексными числами\n'
      '2) Операции с натуральными дробями\n')

mode = input()
if validation(mode):
    print('Введите необходимое действие:\n')
    global mode1
    mode1 = input()
    if mode1 not in '+-*/':
        print('Введены некорректные данные\n'
              'Окончание работы программы')

    elif mode == '1':
        c = 1
        print('Выбран режим вычисления комплексных чисел\n')
        for i in range(2):
            for j in range(2):
                print(f'Введите {words1[j]} числа {i + 1}\n')
                buffer = input()
                validation(buffer)
                if validation(buffer):
                    num1.append(int(buffer))
                else:
                    print('Введены некорректные данные\n'
                          'Окончание работы программы')
                    break
        num2 = [num1[2], num1[3], mode1]
        num1.pop()
        num1.pop()
        res = arithmetic(num1, num2, mode1)
        logging_to_file(res)
        print(res)
    elif mode == '2':
        print('Выбран режим вычисления натуральных дробей\n')
        for i in range(2):
            for j in range(2):
                print(f'Введите {words2[j]} числа {i + 1}\n')
                buffer = input()
                validation(buffer)
                if validation(buffer):
                    num1.append(int(buffer))
                else:
                    print('Введены некорректные данные\n'
                          'Окончание работы программы')
                    break

        num2 = [num1[2], num1[3], mode1]
        num1.pop()
        num1.pop()
        res = fraction(f'{num1[0]}/{num1[1]}', f'{num2[0]}/{num2[1]}', mode1)
        logging_to_file(res)
        print(res)
    else:
        print('Выбранный режим не распознан\n'
              'Окончание работы программы')
else:
    print('Окончание работы программы')
```
Модуль осуществляет взимодействие между пользователем и остальными модулями программы, а также осуществляет валидацию введенных пользователем данных.
