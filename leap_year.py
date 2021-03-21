y=int(input("Enter The year: "))
if(((y%2==0)or (y%400==0))and y%100!=0):
    print("leap Year")
else:
    print("Not Leap year")
