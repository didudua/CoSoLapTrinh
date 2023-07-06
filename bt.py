#bai2:
# def Input():
#     L=[]
#     n=int(input())
#     for i in range(1,n+1):
#         L+=[int(input())]
#     return L
# def tinh(L):
#     print(max(L))
#     print(min(L))

# tinh(Input())
#bai1:
# def Input():
#     L=[]
#     while True:
#         a=input()
#         if a=='': break
#         L.append(a)
#     return L
# def loc(L):
#     KQ=[]
#     for i in L:
#         if i not in KQ: KQ.append(i)
#     print(KQ)

# loc(Input())
#bai3
# def Input():
#     L=[]
#     n=int(input())
#     for i in range(1,n+1):
#         L+=[int(input())]
#     return L
# def Output(L):
#     a=0
#     b=0
#     c=0
#     for i in L:
#         if i >0: a+=1
#         if i %2==0:
#             b+=1
#             c+=i
#     print(a)
#     print(c/b)
# Output(Input())
#Bai4
# a=input()
# L=a.split()
# for i in L:
#     if len(i)>=5:
#         print(i)
#bai5
# L=input()
# for i in L:
#     if i.isnumeric():
#         print(i)