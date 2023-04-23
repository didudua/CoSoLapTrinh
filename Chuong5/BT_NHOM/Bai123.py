def phancap(dau):
    if dau == '*' or dau == '/':
        return 2
    elif dau == '+' or dau == '-':
        return 1
    else:
        return 0
    
def run(nhap):
    LNhap = nhap.split()
    LDau = []
    KQ = []
    for i in LNhap:
        if i.isnumeric(): 
            KQ.append(i) 
        elif i in ['+', '-', '*', '/']: 
            while LDau and LDau[-1] != '(' and phancap(i) <= phancap(LDau[-1]):
                KQ.append(LDau.pop()) 
            LDau.append(i) 
        elif i == '(': 
            LDau.append(i) 
        elif i == ')': 
            while LDau[-1] != '(': 
                KQ.append(LDau.pop()) 
            LDau.pop() 
    while LDau: 
        KQ.append(LDau.pop()) 
    return ' '.join(KQ)

nhap = input()
print(run(nhap)) 