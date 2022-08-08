n=5
for i in range(n):
  for j in range(n):
    if j==i or j+i==n-1 :
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print(" ")