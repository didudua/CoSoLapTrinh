ten = input('Ho ten: ')
day = int(input('So ngay cong: '))
dongiaday = int(input('Don gia ngay cong: '))
phucap = float(input('He so phu cap: '))
ung = int(input('Tam ung: '))
luong = dongiaday*day*phucap
linh = luong-ung
print('Nhan vien '+ten+', Co tien Luong='+str(luong) +
      ', Tam ung='+str(int(ung))+' va Thuc linh='+str(linh))
