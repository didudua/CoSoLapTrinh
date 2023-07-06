# dem so nguyen am a e i o u
x=input()
a=0
e=0
i=0
o=0
u=0
for j in x:
    if j=='a': a+=1
    elif j=='e': e+=1
    elif j=='i': i+=1
    elif j=='o': o+=1
    elif j=='u': u+=1
print(f'''{a}
{e}
{i}
{o}
{u}''')