a = []
b=[]
n=int(input("enter the range=")) 
for i in range(n): 
	number = int(input("Enter A Number: "))
	a.append(number)
print(a[i])

for i in range(n):
    r=1
    for j in range(n):
        if(a[i]!=a[j]):
            r=r*a[j]
        
    b.append(r)

print(b)
