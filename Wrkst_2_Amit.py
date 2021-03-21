dict = {}
uid =[]
name = []
age = []
n = int(input("Plz Enter Number of User U Want to Add: "))
i =0
while(i<n):
     print()
     print("Enter User ",i+1," Details")
     uid.append(int(input("Enter User ID : ")))
     name.append(input("Enter User Name : "))
     age.append(int(input("Enter Your Age : ")))
     
     i=i+1
dict['User Id'] = uid
dict['Name'] = name
dict['Age']  = age
print(end="\n\n")
for k,v in dict.items():
    print(k," : ",v)

