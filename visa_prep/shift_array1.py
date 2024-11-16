n = int(input())
arr = list(map(int,input().split()))[:n]
l = []
for i in range(n):
    if(i!=n-1):
        l.append(arr[i+1])
    else:
        l.append(arr[0])
print(*l)
