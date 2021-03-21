def  take_List(li,Qu_st):
    r=[]
    for i in range(len(li)):
        if(Qu_st in li[i] ):
            r.append(li[i])
    print(r)
li=['sser','ser','song']
q='ss'
take_List(li,q)
