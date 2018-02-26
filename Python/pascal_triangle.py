#!/usr/local/bin/python3
import math

def genPascal(N):
  pascal = [[0 for col in range(N)] for row in range(N)]

  for i in range(N):
    if i == 0:
      pascal[i][0] = 1
      continue

    for j in range(N):
      if j == 0:
        a = 0
      else:
        a = pascal[i-1][j-1]
      b = pascal[i-1][j]
      pascal[i][j] = a + b
  return pascal


n=4
N=int((2*n) + 1)
pascal = genPascal(N)
for i in range(len(pascal)):
  print(pascal[i])
print (pascal[int(N-1)][int(math.ceil(N/2))])
