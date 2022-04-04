#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[13]:


def recurse_factorial(x):
    if x == 0:
        return 1
    else:
        return(x * recurse_factorial(x-1))

x = int(input("Please enter your integer: \n")) 
print("The factorial of the number", x, "is", recurse_factorial(x))


# In[ ]:





# In[ ]:




