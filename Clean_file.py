#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


df(head)


# In[5]:


# read first five values
df.head()


# In[6]:


## read last five values
df.tail()


# In[7]:


# checking columns
df.columns


# In[8]:


df.info()


# In[9]:


#checking for null values 
df.isnull().sum()


# In[10]:


df.dropna(inplace=True)


# In[11]:


df


# In[12]:


df.isnull().sum() 


# In[13]:


df.info()


# In[14]:


# HANDLING MISSING DATA
x = df['Calories'].mean()
print(x)


# In[15]:


df['Calories'].fillna(x,inplace=True)


# In[16]:


df.isnull().sum()


# In[17]:


df['Date'].fillna('2022/05/27',inplace= True)


# In[18]:


df.isnull().sum()


# In[19]:


df.info()


# In[ ]:




