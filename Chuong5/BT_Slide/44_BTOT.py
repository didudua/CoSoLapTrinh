L = [1, 2, 3, 4, 5, 6, 7]

def nhap():
    x = input('nhap x: ')
    k = int(input('vi tri k: '))
    y = input('y thay the x: ')
    return x, k, y

def add(L, x, k):
    if k > len(L):
        L.append(x) # them x vao vi tri cuoi cua day
    else:
        L.insert(k, x) # them x vao vi tri k cua day
    return L

#cau 2
def search(L, x):
    if x in L:
        u = L.index(x)
        return u
    else:
        return None

#cau 3
def delete(L, x):
    if x in L:
        L.remove(x)
    return L

#cau4
def count(L) :
    return len(L)

#cau5
def update(L, x, y):
    if x in L:
        L.insert(L.index(x), y)
        L.remove(x)
    return L

x, k, y = nhap()
print('cau1')
L = add(L, x, k)
print(L)
print('cau2')
u = search(L, x)
print(u)
print('cau3')
L = delete(L, x)
print(L)
print('cau4')
c = count(L)
print(c)
print('cau5')
L = update(L, x, y)
print(L)