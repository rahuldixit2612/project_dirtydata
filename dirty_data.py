#!/usr/bin/env python
# coding: utf-8

# In[1]:
### THIS IS THE CHANGE ON REMOTE AND CHANGES WILL SHOW ON LOCAL ALSO

import pandas as pd
import numpy as np
import seaborn as sn
import sklearn as sk
import matplotlib.pyplot as plt


# In[2]:


# reading file using pandas
df = pd.read_csv('dirtydata.csv')


# In[3]:


df


# In[4]:


# read first five values
df.head()


# In[5]:


## read last five values
df.tail()


# In[6]:


# checking columns
df.columns


# In[7]:


# for complete information about data or table
df.info()


# In[8]:


#checking for null values 
df.isnull().sum()


# In[ ]:





# In[ ]:





# In[ ]:




