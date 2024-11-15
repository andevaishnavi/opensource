t = int(input())
for i in range(0,t):
    x,n = map(int,input().split())
    res = n*(x//10)
    print(res)
