v,c = list(input().split())
if((v == "P" and c == "R") or (v == "S" and c == "P") or (v == "R" and c == "S")):
    print("Vignesh")
elif((c == "P" and v == "R") or (c == "S" and v == "P") or (c == "R" and v == "S")):
    print("Charan")
else:
    print("NULL")
