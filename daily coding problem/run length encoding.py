def encode(Mstr):
    msg=""
    WS=0
    for i in range(len(Mstr)):
        ch=Mstr[i]
        WS=WS+1
        if(i==len(Mstr)-1):
            msg=msg+str(WS)+ch
            break
        else:
            if(ch==Mstr[i+1]):
                pass
            else:
                msg=msg+str(WS)+ch
                WS=0
    return msg
s='AAAABBCCCCD'
print(encode(s))
s='A'
print(encode(s))
