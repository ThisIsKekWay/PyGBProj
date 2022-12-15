# Логирование

from datetime import datetime as dt

def logging_to_file(arithmetic):
    path = "log.csv"
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, "a")
    f.write(f'{time_sign}--> {arithmetic}\n')
    f.close()


    
# Test
# f = [8, 5]
# g = [3, 4]
# k = '-'
# def arithmetic(a, b, symbol_operator): # a и b должны быть тип list  a = [], b =[]
#     complex1 = complex(a[0], a[1])
#     complex2 = complex(b[0], b[1])
#     operation={'+':lambda x, y:x+y,
#                '-':lambda x, y:x-y,
#                '*':lambda x, y:x*y,
#                '/':lambda x, y:x/y,}
#     return f'{complex1} {symbol_operator} {complex2} = {operation[symbol_operator](complex1,complex2)}'
#
# logging_to_file(arithmetic(f, g, k))

