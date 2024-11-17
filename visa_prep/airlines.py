import math
x,n = map(int,input().split())
res = x * 100
rem = n - res
if (rem>res):
    print("0")
else:
    print(math.ceil(rem/100))
