i = 1
while i <= 17:
    n = 15
    while n >= (i-1):
        print(" ", end="")
        n = n-2
    j = 1
    while j <= i:
        print("*", end="")
        j = j+1
    print("")
    i = i+2
