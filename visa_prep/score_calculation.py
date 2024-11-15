t = int(input())
for i in range(0,t):
    x,n = map(int,input().split())
    res = x//10
    res1 = res * n
    print(res1)
