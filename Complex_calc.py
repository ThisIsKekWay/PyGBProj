f = [8, 5]   #  Это
g = [3, 4]   #  для 
k = '-'      #  проверки
def arithmetic(a, b, symbol_operator): # a и b должны быть тип list  a = [], b =[]
    complex1 = complex(a[0], a[1])
    complex2 = complex(b[0], b[1])
    operation={'+':lambda x, y:x+y, 
               '-':lambda x, y:x-y,
               '*':lambda x, y:x*y, 
               '/':lambda x, y:x/y,}
    return f'{complex1} {symbol_operator} {complex2} = {operation[symbol_operator](complex1,complex2)}'

print(arithmetic(f, g, k))
