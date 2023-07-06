while True:
    n=input()
    if n=='': break
    elif 0<=int(n)<=2: print('Tre nho')
    elif 3<=int(n)<=12: print('Tre em')
    elif 13<=int(n)<=19: print('Tuoi teen')
    elif 20<=int(n)<=59: print('Truong thah')
    elif int(n)>=60: print('Nguoi gia')
