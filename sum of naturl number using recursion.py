def rec_sum(n):
    if(n<=1):
        return n
    else:
        return(n+rec_sum(n-1))
print(rec_sum(10))


#10+9+8+7+6+5+4+3+2+1
