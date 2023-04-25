dau=',.;:'
L=input().strip(' ')
L=L.capitalize()
L=list(L)
i=0
while i<len(L):
    if L[i] in dau:
        for j in range(i-1,-1,-1):
            if L[j]==' ':
                L.pop(j)
            else: break
    else:
        i+=1
print(''.join(L))
