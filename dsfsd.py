a=int(input())
sum=0
while(a>0):
    rm=a%10
    sum=sum+rm
    a= a//10
print(sum)
