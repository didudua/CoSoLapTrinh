n = input().split()
tong = 0
N = []
for i in n:
    tong += int(i)
    N.append(str(tong))
kq = ' '.join(N)
print(kq)