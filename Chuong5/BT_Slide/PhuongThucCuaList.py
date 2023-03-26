names = [1, 2, 3, 2, 4, 5]
names.append(6)  # thêm 6 vào cuối dãy names
print(names)
names.insert(0, 7)  # chèn 7 vào vị trí 0 trong dãy names
print(names)
names.insert(-1, 8)
print(names)
u=names.index(2)  # trả về vị trí số 2 trong dãy names
                # ở đây names.index(2)=1
print(u)
names.remove(2)  # xoá số 2 đầu tiên trong dãy names
print(names)
# .sort(): chỉ thực hiện khi trong dãy có cùng kiểu dữ liệu
names.sort()  # sắp xếp các phần tử trong dãy ( mặc định là tăng dần)
print(names)
names.sort(reverse=True) # sắp xếp các phần tử trong dãy giảm dần ( reverse=True)
print(names) 
# nếu dãy là kiểu dữ liệu: sẽ được sắp xếp theo ký tự đầu tiên theo bảng chữ cái alphabet           
names.reverse() # đảo ngược thứ tự các phần tử trong dãy
                # vd: cho dãy [1,2,3,4,5]
                # thực hiện đảo ngược
                # -> [5,4,3,2,1]
print(names)
print(names.count(2)) # thực hiện đếm số 2 có trong list
               # ở đây name.count(2)=2 vì có 2 số 2 trong list
name1=names.copy() # thực hiện copy list names gán cho name1
print(name1)
x=names.pop(2) # thực hiện xoá và lấy ra giá trị thứ 2 trong list
             # nếu để trống vd: .pop() thì mặc định là gí trị cuối trong list
print(names)
print(x)
names.clear() # xoá tất cả các phần tử trong list
print(names)
# chuong 7
str.isdigit() # trả về chuỗi str đó có phải là số hay không vd: a=1000 a.isdigit()= True
              # vd: a=100ABC a[0:2].isdigit()=True\
str.isalpha() #