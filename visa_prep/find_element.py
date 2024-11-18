n = int(input())
arr = list(map(int,input().split()))[:n]
k = int(input())
for i in range(n):
    if(k==arr[i]):
        print(i)
        exit()
print("-1")
