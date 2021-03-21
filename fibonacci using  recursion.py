def fibonacci(x):
    if(x<=1):
        return x
    else:
        return(fibonacci(x-1)+fibonacci(x-2))
a=int(input("Enter The  Range 0 to :"))
for i in range(a+1):
    print(fibonacci(i))
