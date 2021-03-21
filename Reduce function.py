import functools
x=[1,2,3,4,5,6]
print(functools.reduce(lambda a,b:a+b,x))
