def arithmetic(a, b, symbol_operator): # a и b должны быть тип list  a = [], b =[]
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
