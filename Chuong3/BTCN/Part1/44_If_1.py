import math
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a>0 and b>0 and c>0:
 if (a+b) > c and (a+c) > b and (b+c) > a:
    p = (a+b+c)/2
    s = math.sqrt((p*(p-a)*(p-b)*(p-c)))
    print('Dien tich='+str(round(s, 3)))
 else:
    print('Khong hop le')
