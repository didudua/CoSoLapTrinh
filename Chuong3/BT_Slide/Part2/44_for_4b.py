# for i in range(1,18,2):
#     for k in range (i,18,2):
#         print(' ',end="")
#     for j in range(1,i+1):
#            print('*',end="")
#     print('')
#c2
n=9
for i in range(1,10):
    print(' '*(n-i),end='')
    print('*'*(2*i-1))