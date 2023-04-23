def TaoVeSo():
    S=[]
    import random
    S = random.sample(range(1, 50), 6) # random từ 1 đến 49  và lấy 6 số
    S.sort()   
    return S

print(TaoVeSo())