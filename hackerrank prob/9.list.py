n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if(cmd !="print"):
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)




# input like as--
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print
