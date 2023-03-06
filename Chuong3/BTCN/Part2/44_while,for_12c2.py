n = int(input())
# tao bang chia gia tri can
mh=['A','B','C','D','E','F','G','H','K','L']

# tao bién phu luu tri bién lay tuong tng
n_str = str(n)
bienphu = ''

for i in n_str:
    bienphu += mh[int(i)] #+= tuong duong voi bienphu = bienphu+mh[int(i)]

print(bienphu)
