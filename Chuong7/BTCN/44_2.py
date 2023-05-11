
# cau=input()
# cau=cau.strip() 
# tu=cau.lower().split() 
# chucaidau=tu[0] 
# inhoa=chucaidau.title() 
# tu.remove(chucaidau) 
# tu.insert(0,inhoa) 
# vanbanmoi=' '.join(tu) 
# input_str=vanbanmoi.replace(" , ",", ").replace(" ; ","; ").replace(" . ",". ")
# print(input_str)

L=input().strip(' ')
L=L.capitalize()
L=L.split()
L=' '.join(L)
kq=L.replace(' , ',', ').replace(' . ','. ').replace(' ; ','; ').replace(' : ',': ')
print(kq)