x = float(input('x='))
y = float(input('y='))
ch = input('Phep toan:')
if ch == '+':
    print(x, ch, y, '=', x+y,sep='')
elif ch == '-':
    print(x, ch, y, '=', x-y,sep='')
elif ch == '*':
    print(x, ch, y, '=', x*y,sep='')
elif ch == '/':
    if y == 0:
        print('Khong hop le')
    else:
        print(x, ch, y, '=', x/y,sep='')
else:
    print('Khong hop le')
