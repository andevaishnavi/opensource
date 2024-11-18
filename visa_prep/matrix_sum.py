n = int(input())
m = [list(map(int,input().split()))for _ in range(n)]
res =[]
for i in range(n):
    r = sum(m[i])
    c = sum(m[j][i] for j in range(n))
    res.append(r + c)
print(*res)
