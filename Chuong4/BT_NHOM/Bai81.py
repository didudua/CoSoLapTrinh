import math
def nhap():
    a=float(input())
    b=float(input())
    return(a,b)
def canhhuyen(a,b):
    h=math.sqrt(a**2+b**2)
    return(h)
def inkq(h):
    print('Canh huyen:',round(h,1))
x,y=nhap()
h=canhhuyen(x,y)
inkq(h)
 