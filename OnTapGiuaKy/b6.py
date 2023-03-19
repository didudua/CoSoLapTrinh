z=0
y=0
while True:
    n=input()
    if n =='T':break
    elif int(n)%2==0:
        z+=int(n)
        y+=1
print('trung binh cong cac so chan:',z/y)
    