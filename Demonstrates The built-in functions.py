lp=1
ch=0
while(lp==1):
    print("Your option Are: ")
    print(" ")
    print("1.Demonstrate Conversion.")
    print("2.Integer to float Conversion.")
    print("3.Mathematical Functions. ")
    print("4.Date and Time. ")
    print("5.Quit. ")
    ch=int(input("What's your Option: "))
    if(ch==1):
        a=int(input("Enter The Integer Number: "))
        print(bin(a),"  in binary")
        print(oct(a),"  in octal ")
        print(hex(a),"in hexadecimal")
    if(ch==2):
        b=int(input("Enter The Integer: "))
        print("float of ",b," is ",float(b))
    if(ch==3):
        c=float(input("Enter The float value: "))
        import math
        print("The floor value is: ",math.floor(c))
        print("The Round Value is: ",round(c))
        d=int(input("Enter The Integer Number: "))
        print("The Absolute value is: ",math.sqrt(d))
        print("The square root is: ",abs(d))
    if(ch==4):
        import datetime
        today=datetime.date.today();
        print(today)
        print("current Time: ",today.ctime())
        print("today Day: ",today.day)
        print("today month: ",today.month)
        print("today year: ",today.year)
    if(ch==5):
        ch=0
        print("")
        print("")
        print("Have A Nice Day")
        print("")
        print("")
        print("")
        print("")


        
