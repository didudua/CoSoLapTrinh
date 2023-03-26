def nhap():
    s=float(input('Nhap so km:'))
    return s

def tinhtien(s):
    t=4.0
    m=s*1000//140
    t=t+m*0.25
    return(t)
def inkq(t):
    print('So tien phai tra la:',t,'(do la)')
    
s=nhap()
t=tinhtien(s)
inkq(t)