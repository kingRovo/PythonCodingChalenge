#!/usr/bin/env python
# coding: utf-8

# In[37]:


u=int(input("Enter range:  "))
ind =0
for i in range(3,u+1):
    cnt=0
    for j in range(2,i):
        if(i%j==0):
            cnt=1
            break
   
    if(cnt==0):
        if(ind > 0 and i ==ind+2):
            print(ind," ",i)
            ind =i
        else:
            ind = i
        
   
           

        
           
            
            


# In[ ]:





# In[ ]:





# In[ ]:




