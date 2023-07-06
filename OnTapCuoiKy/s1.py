#kt so arstrong
n=input()
c=0
for i in range(len(n)):
    c+=int(n[i])**3
if c == int(n):
    print(True)
else: print(False)
