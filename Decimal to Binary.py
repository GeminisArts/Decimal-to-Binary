#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import linalg as LA
import itertools
from itertools import islice


# In[2]:


def DecToBin(n):
    
    if n<=1:
        return str(n)
    else:
        return DecToBin(n//2) + DecToBin(n%2)


# In[3]:


NewDec = int()
NewDecList = []
repeat = 1

while repeat < 5:
    while NewDec <= 15:
        if repeat == 5:
            break
        NewDec = int(input("Enter an integer: "))
        NewDec2 = list(DecToBin(NewDec))
    
        if NewDec > 15:
            print("This will not be added to NewDecList.\n")
        elif NewDec <= 15:
            NewDecList.append(NewDec)
            print("This will be added to NewDecList.\n")
        
        repeat += 1


# In[4]:


Results = []

Input = NewDecList

for i in Input:
    Input = ('{num:04b}'.format(num=i))
    Results.append(Input)

length = [1,1,1,1]
Results2 = iter(Results)
Output = [list(islice(Results2, elem)) for elem in length]
ResultList = [[int(i) for i in sub] for i in Output for sub in i]


# In[5]:


ResultArray = np.array(ResultList)
print(ResultArray)


# In[6]:


ResultMatrix = np.matrix(ResultArray)
print(ResultMatrix)


# In[ ]:




