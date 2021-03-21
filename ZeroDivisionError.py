try:
    a=9/3

    print(a)
except ZeroDivisionError:
    print("Zero divided error")
finally:
    print("Always execute")
