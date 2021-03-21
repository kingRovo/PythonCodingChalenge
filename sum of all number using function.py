def sumAll(*a):
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]
    return sum

pr=sumAll(12,23,34,45,54)
print(pr)


