from Bai118 import createDeck,shuffle

def deal(BoBai,n):
    tays=[]
    for i in range(n):
        tay=[]
        for j in range(5):
            bai=BoBai.pop(0)
            tay.append(bai)
        tays.append(tay)
    return tays,BoBai
n=int(input('Nhap so tay: '))
tays,BoBai=deal(shuffle(createDeck()),n)
for i in range(n):
    print('Tay',i+1)
    print(tays[i])
print('Bo Bai Con Lai','\n',BoBai)