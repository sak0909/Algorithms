import math
I,i=input,int
n=i(I())
a=9999 if n>0 else 0
for t in I().split():
 t=i(t);a = t if abs(t)<abs(a)else a;a = abs(t)if t==-a else a
print(a)