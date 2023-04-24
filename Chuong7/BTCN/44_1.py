L=input()
hoa=0
thuong=0
so=0
khac=0
for i in L:
    if i.isupper():
        hoa+=1
    elif i.islower():
        thuong+=1
    elif i.isdigit():
        so+=1
    else:
        khac+=1
print(f'''In hoa: {hoa}
In thuong: {thuong}
Chu so: {so}
Khac: {khac}
      ''')