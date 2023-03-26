u=0
for i in range(1,1000):
    for j in str(i):
        if int(j)==9:
            print(i,end='\t') 
            u+=1
            break
print(u)