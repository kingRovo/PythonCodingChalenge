def ask(k):
    s=1;
    if k=='lock':
        a=input("Name: ")
        b=int(input("Password: "))
        s=s+1
    else:
        print("Lock Program ")
    if(s==2):
        print("Welcome ",a," bhai sbb Theek thaak ")
        print("your password:- ",b)
n=input("Lock Or Unlock: ")
ask(n)   
