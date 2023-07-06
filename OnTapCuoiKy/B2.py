# x='abc'
# y='de'
# z='mnt'
# a=''
# kq=[]
# for i in x:
#     for j in y:
#         for k in z:
#             a=i+j+k
#             kq.append(a)

# print(f'''{kq}
# do dai chuoi {len(kq)}''')
# x=[i for i in range(10)]
# X1=[]
# X2=[]
# X3=[]
# for x1 in x:
#     for x2 in x:
#         for x3 in x:
#             if x1+x2+x3==15:
#                 X1+=[x1]
#                 X2+=[x2]
#                 X3+=[x3] 
# print(f'''{X1}
# {X2}
# {X3}
# co {len(X1)+len(X2)+len(X3)} cach chon''')
# ax+by=c x=(c-by)/a
# dx+ey=f y=(f-dx)/e
a,b,c,d,e,f=[float(i) for i in input().split()]
if a/d != b/e: 
    x=(c/b-f/e)/(a/b-d/e)
    y=(f-d*x)/e
    print(f'{"{:.2f}".format(x)} {"{:.2f}".format(y)}')
elif a/d == b/e != c/f : print('VONGHIEM')
elif a/d == b/e == c/f : print('VOSONGHIEM')