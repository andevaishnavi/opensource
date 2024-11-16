n ,m = map(int,input().split())
res = []
res1 =[]
arr = list(map(int,input().split()))[:n]
for i in arr:
    if((i % m) == 0):
        res.append(i)
    else:
        res1.append(i)
result = sum(res) - sum(res1)
print(result)
