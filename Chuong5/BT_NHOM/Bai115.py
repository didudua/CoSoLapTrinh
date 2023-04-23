def Input():
    L=input()
    return list(L)
def PigLatin(L):
    NgA=['a', 'e', 'o', 'i', 'u']
    if L[0].lower() in NgA:
        L=L+['way']
    elif L[0].lower()=='t' and L[1].lower()=='h':
        L=L[2:]+L[:2]+['ay']
    else:
        L=L[1:]+L[:1]+['ay']
    return ''.join(L)

print(PigLatin(Input()))