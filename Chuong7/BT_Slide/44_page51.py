def run(L):
    return L.lower(),L.upper()
print('Bai 7.4:')
L=input()
h,H=run(L)
print(h)
print(H)
def dem(L):
    so=0
    chu=0
    for i in L:
        if i.isnumeric():
            so+=1
        elif i.isalpha():
            chu+=1
    return so,chu
print('Bai 7.5:')
so,chu=dem(input())
print('Chu cai:',chu)
print('Chu so:',so)
