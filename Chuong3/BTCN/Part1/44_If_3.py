x = float(input('x='))
y = float(input('y='))
ch = input('Phep toan:')
if ch == '+':
    print(x, ch, y, '=', x+y)
elif ch == '-':
    print(x, ch, y, '=', x-y)
elif ch == '*':
    print(x, ch, y, '=', x*y)
elif ch == '/':
    if y == 0:
        print('Khong hop le')
    else:
        print(x, ch, y, '=', x/y)
else:
    print('Khong hop le')
