def nhap():
    n=int(input('n='))
    return n

def sodoi(n):
    if n < 1 or n > 12:
        return ''
    elif n == 1:
        return 'first'
    elif n == 2:
        return 'second'
    elif n == 3:
        return 'third'
    elif n == 4:
        return 'fourth'
    elif n == 5:
        return 'fifth'
    elif n == 6:
        return 'sixth'
    elif n == 7:
        return 'seventh'
    elif n == 8:
        return 'eighth'
    elif n == 9:
        return 'ninth'
    elif n == 10:
        return 'tenth'
    elif n == 11:
        return 'eleventh'
    elif n == 12:
        return 'twelfth'
def inkq(kq):
    print (kq)
if __name__ == '__main__':
    n=nhap()
    kq=sodoi(n)
    inkq(kq)