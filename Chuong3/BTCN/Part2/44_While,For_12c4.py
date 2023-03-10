n = int(input(""))
n_str = ""
for i in str(n):
    if i == "0":
        n_str += "A"
    elif i == "1":
        n_str += "B"
    elif i == "2":
        n_str += "C"
    elif i == "3":
        n_str += "D"
    elif i == "4":
        n_str += "E"
    elif i == "5":
        n_str += "F"
    elif i == "6":
        n_str += "G"
    elif i == "7":
        n_str += "H"
    elif i == "8":
        n_str += "K"
    elif i == "9":
        n_str += "L"
print(n_str)