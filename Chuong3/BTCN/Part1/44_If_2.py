a = float(input('M1='))
b = float(input('M2='))
c = float(input('M3='))
s = float(input('S='))
if s <= 100:
    p = s*a
elif s >= 101 and s <= 150:
    p = 100*a+(s-100)*b
elif s >= 151:
    p = 100*a+(s-150)*c+50*b
print('Phai tra='+str(int(p)))
