w=['bed','bath','bedbath','and','beyond']

b=""
li=[]
s="bedand"
for i in s:
    b+=i
    if(b in w ):
        li.append(b)
      

        b=""
print(li)        
