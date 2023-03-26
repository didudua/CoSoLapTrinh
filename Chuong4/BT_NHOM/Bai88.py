def tamgiac(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True

a = float(input("Do dai canh a: "))
b = float(input("Do dai canh b: "))
c = float(input("Do dai canh c: "))

if tamgiac(a, b, c):
    print("3 canh nay có the tao thanh 1 tam giac")
else:
    print("3 canh nay khong the tao tham 1 tam giac")
