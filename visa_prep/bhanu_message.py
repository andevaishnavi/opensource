n = input()
a = list(n)
if((a[0]=="+") and (a[1].isdigit()) and (a[2].isdigit()) and (a[3]==" ") and (len(a)==14)):
    print("Correct")
else:
    print("Incorrect")
