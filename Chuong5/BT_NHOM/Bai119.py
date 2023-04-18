from Bai118 import createDeck,shuffle
def deal(BoBai):
    tay1=[]
    tay2=[]
    tay3=[]
    tay4=[]
    for i in range(0,20,4):
        tay1+=[BoBai[i]]
        tay2+=[BoBai[i+1]]
        tay3+=[BoBai[i+2]]
        tay4+=[BoBai[i+3]]
    for x in tay1:
        if x in BoBai:
            BoBai.remove(x)
    for x in tay2:
        if x in BoBai:
            BoBai.remove(x)
    for x in tay3:
        if x in BoBai:
            BoBai.remove(x)
    for x in tay4:
        if x in BoBai:
            BoBai.remove(x)
    return BoBai,tay1,tay2,tay3,tay4
BoBai,tay1,tay2,tay3,tay4=deal(shuffle(createDeck()))
print('Tay1','\n',tay1)
print('Tay2','\n',tay2)
print('Tay3','\n',tay3)
print('Tay4','\n',tay4)
print('Bo Bai:','\n',BoBai)