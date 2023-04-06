#aPIkey: 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
#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
# n = int(input("Nhập số n: "))
# S = sum([1/i for i in range(2,n+1)])

# print("{:.4f}".format(S)) # làm tròn chữ số thập phân thứ 4 chính xác vd 0.5000

# n=int(input())
# s=''
# if n<0: n*=-1
# for i in str(n):
#    s+=str(i)
# print(len(s))

# a = int(input("Enter first integer: "))
# b = int(input("Enter second integer: "))

# # Ước CHung lớn nhất
# def gcd(a,b):
#     if(b == 0):
#         return a;
#     else:
#         return gcd(b, a % b)

# print("GCD of", a,"and", b,"is", gcd(a, b))

# nhập vào số 123 và in ra 321

# n=int(input())
# s=''
# for i in str(n):
#  s=str(i)+s
# print(s)
# a, b = input().split()
# a = int(a)
# b = int(b)
# for i in range(b+1, a, -1):
#     if i % 3 == 0:
#         print(i, end=' ')
#         continue
#     else: s=1
# if s==1: print('NOT FOUND')


# num = int(input("Nhập vào một số nguyên: "))

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "không phải là số nguyên tố")
#             break
#     else:
#         print(num, "là số nguyên tố")
# else:
#     print(num, "không phải là số nguyên tố")
a=input()
xet=['.','?','!']
a=a.capitalize() 
for i in range(len(a)):
    if a[i] in xet:
        for j in range(i+1,len(a)):
            if a[j]!=' ': 
                a=a[:j]+a[j:].capitalize()
                break

print(a)

