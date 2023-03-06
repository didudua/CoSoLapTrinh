n=int(input())
mh=['A','B','C','D','E','F','G','H','K','L']
#stt:0   1   2   3   4   5   6   7   8   9
while n>=0 and n<10000:
    if n<10: print(mh[n]) #n=1,2,3,4,5,6,7,8,9 ung voi thu tu trong mh vd:n=1 -> tt 1 tuong ung voi 'B'
    elif n>=10 and n<100: print(mh[n//10],mh[n%10],sep='')
                                 #vd:n=24
                                 #n//10: chia lay phan nguyen: 24//10 = 2-> tt 2 tuong ung voi 'C'
                                 #n%10: chia lay phan du:      24%10 = 4-> tt 4 tuong ung voi 'E'
                                 #sep='': xoa khoan cach       -> 24 = CE
    elif n>=100 and n<1000: 
        i=n//10 #vd: n=123 : i=123//10=12
        print(mh[i//10],mh[i%10],mh[n%10],sep='')
        # i//10=12//10 =1-> tt 1 tuong ung voi 'B'
        # i%10= 12%10 =2-> tt 2 tuong ung voi 'C'
        # n%10 = 123%10 =3-> tt 3 tuong ung voi 'D'
        #--> 123 = BCD
    elif n>=1000: #vd n = 1234
        i=n//100  # i=n//100 = 1234//100 = 12
        j=n%100   # j=n%100 = 1234%100 = 34
        print(mh[i//10],mh[i%10],mh[j//10],mh[j%10],sep='')
        # i//10 = 12//10 = 1 -> tt 1 tuong ung voi 'B'
        # i%10 = 12%10 = 2-> tt 2 tuong ung voi 'C'
        # j//10 = 34//10 = 3 -> tt 3 tuong ung voi 'D'
        # j%10 = 34%10 = 4 -> tt 4 tuong ung voi 'E'
        #--> 1234 = BCDE
    n=n*-1 # de ket thuc vong lap
           # tai de o phan while,for nen dung while,for, chu k can co lenh while van chay dc, chi dung moi lenh if,elif
        