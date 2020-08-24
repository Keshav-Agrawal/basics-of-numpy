#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list1=[1,2,3,4,5]
list1


# In[2]:


array1=np.array(list1)
array1


# In[3]:


matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix1


# In[4]:


array2=np.array(matrix1)
array2


# In[5]:


arr1=np.arange(1,18,2)
arr1


# In[6]:


arr1.reshape(3,3)


# In[7]:


arr=np.arange(10)
arr


# In[8]:


ranarr=np.random.randint(1,10,10)
ranarr


# In[9]:


arr4=np.arange(1,6)
arr4


# In[10]:


arr4.reshape(5,1)


# In[11]:


ranarr.shape


# In[12]:


arr5=np.arange(2,12)
arr5


# In[13]:


arr5[2]


# In[14]:


arr5[3]


# In[15]:


arr5[8]


# In[16]:


arr5=np.arange(2,11,2)
arr5


# In[17]:


arr5[2:5]=100
arr5


# In[18]:


matrix3=np.arange(1,26)
matrix3


# In[19]:


matrix3.reshape(5,5)


# In[30]:


submatrix=matrix3.reshape(5,5)[1:4,1:4]
submatrix


# In[ ]:




