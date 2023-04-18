def createDeck():
    BoBai=[]
    Bai=['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    Chat=['h','d','c','s'] # cơ rô chuồn bích
    for j in range(4):
        for i in range(13):
            BoBai=BoBai+[Bai[i]+Chat[j]]
    return BoBai       
   
def shuffle(BoBai):
    from random import shuffle,randint
    # shuffle(BoBai) xáo trộn các phần tử trong BoBai
    for i in range(len(BoBai)):
        j = randint(0, len(BoBai) - 1)
        BoBai[i], BoBai[j] = BoBai[j], BoBai[i]
    return BoBai
if __name__ == "__main__":
    print('Bo Bai:','\n',createDeck())
    print('Bo Bai duoc xao:','\n',shuffle(createDeck()))
