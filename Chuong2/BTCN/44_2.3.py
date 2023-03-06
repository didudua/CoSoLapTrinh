import math
print('Nhap hai canh ke cua tam giac vuong:')
a = int(input())
b = int(input())
print('Canh ke thu nhat la: '+str(a)+', canh ke thu hai: ' +
      str(b)+', co canh huyen =', round(math.sqrt(a*a+b*b), 2))
