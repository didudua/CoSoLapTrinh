# import random
# # 1: Búa, 2: Kéo, 3: Bao
# while True:
#  n=int(input('Nguoi: '))
#  if n==0: break
#  m=random.randint(1,3)
#  print('May:',m)
#  if n==m: print('Ket qua:'+' Hoa')
#  elif n==1 and m==2: print('Ket qua:'+' Nguoi thang')
#  elif n==2 and m==3: print('Ket qua:'+' Nguoi thang')
#  elif n==3 and m==1: print('Ket qua:'+' Nguoi thang')
#  elif n==2 and m==1: print('Ket qua:'+' Nguoi thua')
#  elif n==3 and m==2: print('Ket qua:'+' Nguoi thua')
#  elif n==1 and m==3: print('Ket qua:'+' Nguoi thua')

import random
# 1: Búa, 2: Kéo, 3: Bao

def sosanh(n,m):
  if n==m: print('Ket qua:'+' Hoa')
  elif n==1 and m==2: print('Ket qua:'+' Nguoi thang')
  elif n==2 and m==3: print('Ket qua:'+' Nguoi thang')
  elif n==3 and m==1: print('Ket qua:'+' Nguoi thang')
  elif n==2 and m==1: print('Ket qua:'+' Nguoi thua')
  elif n==3 and m==2: print('Ket qua:'+' Nguoi thua')
  elif n==1 and m==3: print('Ket qua:'+' Nguoi thua')
while True:
 n=int(input('Nguoi: '))
 if n==0: break
 m=random.randint(1,3)
 print('May:',m)
 sosanh(n,m)
 