n=5
t=5
for i in range(n,0, -1):
    if(i==5):
        print(t)
        t=0
    else:
        b=n-i
        t=t+i+b;
        if(t==5):
            print(i,b)
            b=0
            t=0

                
