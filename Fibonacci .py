#!/usr/bin/env python
# coding: utf-8

# In[6]:


n = int(input("enter n value:"))
a=0
b=1
c=0
while a <= n:
    a = b
    b = c
    c = a + b
    print(c,end=" ")
    


# In[ ]:




