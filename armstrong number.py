n=int(input("Enter Number: "))
t=n
sum=0
while(n>0):
    r=n%10
    sum=sum+r*r*r
    n=n//10
if(t==sum):
    print("Armstrong ")
else:
    print("Not Armstrong")
