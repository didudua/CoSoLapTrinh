def nhap():
    list=[]
    while len(list)<=9:
        n= int(input())
        list=list+[n]
    x=int(input('x='))
    for i in range(len(list)):
        if list[i]==5: 
            list[i]=x
    return list,x
def thay(list,x):
    if x in list:
        list=[n for n in list if n!=x]
    return list
print('Nhap 10 so nguyen:')
list,x=nhap()
print('Cau a:')
print(list)
print('cau b:')
print(thay(list,x))
