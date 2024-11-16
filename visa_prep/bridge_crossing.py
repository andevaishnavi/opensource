x,y,z = map(int,input().split())
c = 0
r = x+y
while(r<=z):
    r += x
    c += 1
print(c)
