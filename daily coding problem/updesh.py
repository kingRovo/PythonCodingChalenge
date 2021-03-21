def hello(n):
    df=[i for i in range(n+1)]
    df[0]=df[1]=df[2]=1
    df[3]=2
    for i in range(4,n+1):
        df[i]=df[i-1]+df[i-3]+df[i-4]
        return df[n]
n=5
print(hello(n))
