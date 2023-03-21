
def LaSoNguyenTo(x):
    if x==2 : return True
    for i in range(2,x):
        if x%i==0: 
            return False
        else: u=True
    return u
def SoHople(x):
    if x<=1: return True
    else: return False
def NhapVaDem(): 
    print('Nhap day so:')
    kq=0  
    while True:
        x=int(input())
        if SoHople(x): break
        else: 
            if LaSoNguyenTo(x): kq+=1
    return kq
        
def InKQ(kq):
    print('Co',kq,'so nguyen to') 


kq=NhapVaDem()
InKQ(kq)