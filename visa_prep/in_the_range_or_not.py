t = int(input())
for _ in range(0,t):
    x = list(map(int,input().split()))
    for i in x:
        if((i>=67) and (i<=45000)):
            print("YES")
        else:
            print("NO")
