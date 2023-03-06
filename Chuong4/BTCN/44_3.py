def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def giaipt(a,b,c):
        from math import sqrt
        denta=b*b-4*a*c
        if denta>0:
            x1=(-b+sqrt(denta))/2*a
            x2=(-b-sqrt(denta))/2*a  
        elif denta==0:
            x1=x2=-b/2*a
        elif denta<0:
            x1=True
            x2=False
        return x1,x2
def inkq(x1,x2):
    if x1==True and x2==False:
        print('Phuong trinh vo nghiem')
    elif x1>x2 or x1<x2:
        print('Phuong trinh co hai nghiem')
        print('x1=',x1,sep='')
        print('x2=',x2,sep='')
    elif x1==x2:
        print('Phuong trinh co nghiem kep')
        print('x1=x2=',x1,sep='')
a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)
