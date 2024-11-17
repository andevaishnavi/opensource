n = int(input())
arr = list(map(int,input().split()))[:n]
s = sorted(arr)
if(arr == s):
    print("true")
else:
    print("false")
