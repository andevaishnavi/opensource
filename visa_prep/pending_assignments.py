x,y,z = list(map(int,input().split()))
res = x * y
t = z * 24 * 60
if(res<=t):
    print("YES")
else:
    print("NO")
