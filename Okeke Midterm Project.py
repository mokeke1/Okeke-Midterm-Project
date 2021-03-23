#!/usr/bin/env python
# coding: utf-8

# In[9]:


#1
import numpy as np
ini_array = [2, 4, 6, 8, 4, 5, 2, 1, 9, 0, 4, 6, 7, 4, 3, 2, 1, 9, 10, 3, 7, 9, 6, 0, 1, 3, 5, 6, 7, 8, 9, 10, 2, 3, 6, 8, 9, 10, 6, 7, 4, 3]
unique, frequency = np.unique(ini_array, return_counts = True)
for i in range(0, 11):
    print(str(unique[i])+':'+str(frequency[i]))


# In[2]:


import matplotlib.pyplot as plt
plt.bar(unique, frequency, align = 'center', alpha = 0.5)
plt.show()


# In[13]:


import json
dictionary = {}
for i in range (0, 11):
    dictionary[i] = str(frequency[i])
j = json.dumps(dictionary)
j
f = open("mesoma.json", "w")
f.write(j)
f.close()
f = open("mesoma.json", "r")
f.read()


# In[186]:


#2
import pandas as pd
data = pd.read_csv('/Users/mesomaokeke/Downloads/Amazon-Orders.csv')
data.columns = data.columns.str.strip()
data['Order Date']
data.head()


# In[187]:


data.shape


# In[188]:


data = data.fillna(0)
data.head()


# In[189]:


data["Total Charged"] = data["Total Charged"].str.replace('$','').astype(float)
data.head()


# In[190]:


data["Total Charged"].sum()


# In[191]:


data["Total Charged"].mean()


# In[192]:


data["Total Charged"].median()


# In[193]:


data["Total Charged"].max()


# In[194]:


data["Total Charged"].min()


# In[195]:


data["Tax Charged"] = data["Tax Charged"].str.replace('$','').astype(float)
data.head()


# In[196]:


data["Tax Charged"].sum()


# In[197]:


data["Tax Charged"].sum() / data["Total Charged"].sum()


# In[198]:


data['Order Date'] = pd.to_datetime(data['Order Date'])
data.head()


# In[199]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[200]:


data.plot.bar(x='Order Date', y='Total Charged', rot=90)


# In[205]:


data.plot.bar(x='Order Date', y='Total Charged', rot=90, figsize=(25,10))


# In[206]:


everyday_orders = data.groupby('Order Date').sum()["Total Charged"]
everyday_orders.head()


# In[207]:


everyday_orders.plot.bar(figsize=(25,10))


# In[208]:


everyday_orders.plot.bar(figsize=(25, 10), color='maroon')


# In[ ]:





# In[ ]:




