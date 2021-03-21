l=int(input("Enter lower range:  "))
u=int(input("Enter Upper range:  "))
for n in range(l,u+1):
    cnt=0
    for i in range(2,n):
        if(n%i==0):
            cnt=1
            break
    i+=1
    if(cnt==0):
        print(n)
    n+=1
                
            
