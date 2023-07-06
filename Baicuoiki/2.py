def demsnt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
kq = 0
for i in range(2, n + 1):
    if demsnt(i):
        kq += 1
print(kq)