def sai(n):
    li=[0]*(n+1)
    li[0]=1
    for i in range(1,n):
        for j in range(i,n+1):
            li[j]+= li[j-i]
    return li[n]
print(sai(5))
