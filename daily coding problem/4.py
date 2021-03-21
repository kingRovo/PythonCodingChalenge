a=[]
n=int(input("Range: "))
for i in range(1,n+1):
    num=int(input("Enter Values: "))
    a.append(num)
for i in range(1,n+1):
    if(i not in a):
        print(i)


    
    
