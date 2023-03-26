def nhap():
    ch=str(input("Phep toan:"))
    return ch
def inkq(ch):
    if ch=="+" or ch=="-":
        print(1)
        print("La toan tu")
    elif ch=="*" or ch=="/":
        print(2)
        print("La toan tu")
    elif ch=="**":
        print(3)
        print("La toan tu")
    else:
        print(-1)
        print("Khong la toan tu")
ch=nhap()
inkq(ch)

    

    
    
    
        