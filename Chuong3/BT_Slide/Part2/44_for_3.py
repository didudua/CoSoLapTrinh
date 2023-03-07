# u=1
# for i in range(1,10):
#   for j in range(i,i*9+1,u): 
#       print(j,end="\t")
#   u=u+1
#   print("\n")
u=1
for i in range(1,10):
  for j in range(1,10): 
      print(j*i,end="\t")
  u=u+1
  print("\n")