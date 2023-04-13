# cho một dãy số, xét tất cả trường hợp chuỗi các số
# sao cho chuỗi đó số chẵn và số lẻ xen kẽ nhau
# rồi tìm ra độ dài của chuỗi dài nhất
# input: 1 2 2 3 4 3 6 7 8 4 6 7
# output: chuoi chan le dai nhat: 2 3 4 3 6 7 8
       # do dai chuoi: 7
L='122343678467'
# def xet(L):
#     n = 1
#     for i in range(len(L)-1):
#         u = 1
#         for j in range(i+1, len(L)):
#             if (int(L[j]) % 2 == 0 and int(L[j-1]) % 2 != 0) or (int(L[j]) % 2 != 0 and int(L[j-1]) % 2 == 0):
#                 u += 1
#             else:
#                 break
#         if u > n:
#             n = u
#     return n
def xet(L):
    u = 1
    a = 1
    
    for i in range(1, len(L)):
        if (int(L[i]) % 2 == 0 and int(L[i-1]) % 2 != 0) or (int(L[i]) % 2 != 0 and int(L[i-1]) % 2 == 0):
            a += 1
            u = max(u, a)
        else:
            a = 1
    return u

print(xet(L))