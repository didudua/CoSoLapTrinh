while True:
    mk = input('Nhap mat khau: ')
    if len(mk) < 8:
        print('Khong hop le')
    elif not any(x.isupper() for x in mk):
        print('Khong hop le')
    elif not any(x.islower() for x in mk):
        print('Khong hop le')
    elif not any(x.isdigit() for x in mk):
        print('Khong hop le')
    else:
        print('Hop le')
        break
