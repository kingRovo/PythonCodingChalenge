str="updesh yadav"
ab=[]
dup=[]
for i in str:
    if i not in ab:
        ab.append(i)
    else:
        if i not in dup:
            dup.append(i)
print("dup= ",dup)

