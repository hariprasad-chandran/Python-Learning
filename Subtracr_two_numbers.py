#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add_two_numbers(a,b):
    return a+b
add_two_numbers(5,8)


# In[20]:


def subtract_two_numbers(a,b):
   return a-b
a=int(input("Enter the value for a: "))
b=int(input("Enter the value for b: "))

if a-b < 0:
    print("Negative")
else:
    print(subtract_two_numbers(a,b))


# In[ ]:




