n = int(input())
mh = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L']
if n >= 0 and n < 10000:
    if n < 10:
        print(mh[n])
    elif n >= 10 and n < 100:
        print(mh[n//10], mh[n % 10], sep='')
    elif n >= 100 and n < 1000:
        i = n//10
        print(mh[i//10], mh[i % 10], mh[n % 10], sep='')
    elif n >= 1000:
        i = n//100
        j = n % 100
        print(mh[i//10], mh[i % 10], mh[j//10], mh[j % 10], sep='')
