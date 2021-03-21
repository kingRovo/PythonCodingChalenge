def swap_case(s):
    a=""
    for i in s:
        if(i.isupper==True):
            a=a+i.lower()
        else:
            a=a+i.upper()
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
