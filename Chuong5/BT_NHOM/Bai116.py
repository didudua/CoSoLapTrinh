def Input():
    L=input()
    return list(L)
def PigLatin(L):
    NgA=['a', 'e', 'o', 'i', 'u']
    dau=['?','!','.']
    x=[]
    if L[-1] in dau:
        x=L.pop(-1)
    if L[0].lower() in NgA:
        S=L+['way']+[x]
    elif L[0].lower()=='t' and L[1].lower()=='h':
        S=L[2:]+L[:2]+['ay']+[x]
    else:
        S=L[1:]+L[:1]+['ay']+[x]
    if L[0].isupper():
        for i in range(len(L)):
            S[i]=S[i].lower()
        S[0]=S[0].upper()
    return ''.join(S)

print(PigLatin(Input()))