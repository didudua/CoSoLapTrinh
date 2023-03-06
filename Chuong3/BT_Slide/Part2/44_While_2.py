n = int(input('n='))
i = 1
if n>0 and n<=50:
    while i <= n:
        print(i, end=" ")
        i = i+1
        J = i
        while J % 10 == 1:
            print("")
            J = J+1
