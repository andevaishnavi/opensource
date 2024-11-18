s = input()
r = s.lower()
c1 = 0
c2 = 0
for i in r:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        c1 += 1
    elif i.isalpha():
        c2 += 1
print(str(c1)+","+str(c2))
