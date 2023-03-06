while True:
    a = float(input('a='))
    b = float(input('b='))
    pt = input('Toan tu:')
    if a == int(a):
        a = int(a)
    elif b == int(b):
        b = int(b)
    if pt == '+':
        print(a, pt, b, '=', a+b, sep='')
    elif pt == '-':
        print(a, pt, b, '=', a-b, sep='')
    elif pt == '*':
        print(a, pt, b, '=', a*b, sep='')
    elif pt == '/':
        print(a, pt, b, '=', a/b, sep='')
    c = input('Tiep tuc:')
    if c == 't' or c == 'T':
        break
