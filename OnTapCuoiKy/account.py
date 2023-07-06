# cslt6.41 130104 tuan nguoi gia 514140
# cslt6.44 151204
# cslt6.15 060604 khoa
# cslt6.19 200304 long
# cslt6.31 280904 0796732045quann 
# cslt3.30 thuylinh301203 020104 
# cslt7.47 Tuan0501@ hoặc 050104 514239
# n=int(input('n='))
# u=[]
# j=0
# for x in range(2,9999999):
#     for i in range(2,x):
#         if x%i==0: break
#     else: u+=[str(x)]
#     if len(u)==n: break
# print(', '.join(u))

n=(input())
n=n.capitalize()
n=n.strip()
n=list(n)
i=0
while i<len(n):
    if n[i]=="," or n[i]==";" or n[i]==":"or n[i]==".":
        if n[i-1]==" ":
            del(n[i-1])
        else:
            break
    else:
        i=i+1
print("".join(n))