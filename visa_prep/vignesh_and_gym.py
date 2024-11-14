x,y,z = list(map(int,input().split()))
if(z>=x):
    if(x+y <= z):
        print("2")
    else:
        print("1")
else:
    print("0")
