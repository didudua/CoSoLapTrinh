print('Nhap 10 so nguyen:')
num=[]
while len(num)<=9:
    n= int(input())
    num=num+[n]
x=int(input('So nguyen X: '))
for i in range(len(num)):
    if num[i]==5: 
        num[i]=x
print(num)
if x in num:
    num=[n for n in num if n!=x]
    # num = [(for)chay n trong day num if n khac x thi in n]
    print(num)
    
