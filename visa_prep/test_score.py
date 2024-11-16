n,x,y = list(map(int,input().split()))
if((y%x==0) and (x*n >=y)):
    print("YES")
else:
    print("NO")
