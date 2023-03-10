n = int(input(""))
n_str = ""
while n > 0:
    S = n % 10
    if S == 0:
        n_str = "A" + n_str
    elif S == 1:
        n_str = "B" + n_str
    elif S == 2:
        n_str = "C" + n_str
    elif S == 3:
        n_str = "D" + n_str
    elif S == 4:
        n_str = "E" + n_str
    elif S == 5:
        n_str = "F" + n_str
    elif S == 6:
        n_str = "G" + n_str
    elif S == 7:
        n_str = "H" + n_str
    elif S == 8:
        n_str = "K" + n_str
    elif S == 9:
        n_str = "L" + n_str
    n //= 10
print(n_str)