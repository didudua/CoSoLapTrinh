n = int(input())
mh = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L']
n_str = str(n)
bienphu = ''
for i in n_str:
    bienphu += mh[int(i)]
print(bienphu)
