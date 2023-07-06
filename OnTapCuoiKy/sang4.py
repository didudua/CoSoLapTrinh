kt1='!()-[];:"\,<>./?@#$%^&*_~'
kt2=["'",'{','}']
a=input()
for i in a:
    if i not in kt1 and i not in kt2:
        print(i,end='')

# dau='!'+'()'+'-'+'[]'+'{}'+';:'+"'"+'"'+'\,<>./?@#$%^&*_~'
# chuoi=input()
# L=[]
# for i in chuoi:
#     L.append(i)
# for i in range(len(L)-1,-1,-1):
#     if L[i] in dau:
#         del(L[i])
# chuoimoi=''.join(L)
# print(chuoimoi)