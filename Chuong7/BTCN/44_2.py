dau=',.;:'
L=input().strip(' ')
L=L.capitalize()
for j in range(2,len(L)):
    L= ''.join(L.split(j*' '))
L=list(L)
i=0
while i<len(L):
    if L[i] in dau:
        if L[i-1]==' ':
            L.pop(i-1)
    i+=1
print(''.join(L))
