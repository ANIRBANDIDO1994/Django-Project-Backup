#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import string


# In[10]:


path = 'C:/Users/Anirvan Chakraborty/Desktop/BAT BD Master File for Financial Ratios -July 21 (1)1.csv'
table = pd.read_csv(path)
print(table)


# In[12]:


path = 'C:/Users/Anirvan Chakraborty/Desktop/table-4.csv'
c_f_table = pd.read_csv(path)
c_f_table


# In[17]:


df = c_f_table.rename(columns={"Unnamed: 0":"Name", "For the period ended 31 March 2020 ":"31 March 2020", "For the year ended 30 June 2019 ":"30 June 2019"}, errors="raise")
df


# In[18]:


new_header = df.iloc[0] #grab the first row for the header
#df.columns.values[0] = 'Names'
#df.columns.drop(list(df.filter(regex='Note')))
df.dropna(how='all', axis=1, inplace=True)
df = df.loc[:, df.columns.notnull()]
df


# In[20]:


df1 = df.replace(np.nan, '0.0', regex=True)
df1


# In[22]:


TotalcolumnArray = list(df1.columns)
TotalcolumnArray.pop(0)
print(TotalcolumnArray)
for i in TotalcolumnArray:
    df1[i] = df1[i].astype(str)
    df1[i] = df1[i].apply(lambda x:''.join([i.replace('$','') for i in list(x)]))
    df1[i] = df1[i].apply(lambda x:''.join([i.replace('(','-').replace(',','').replace(')','') for i in list(x)]))
    df1[[i]] = df1[[i]].apply(pd.to_numeric, errors='coerce')
df1 = df1.replace(np.nan, '0.0', regex=True)
df1


# In[25]:


conditions = [
            (df1['Name'].str.contains("^Net profit", na=False, case=False)),#Net profit for the period     
        ]

# create a list of the values we want to assign for each condition
values = ['NET_PROFIT' ]

# create a new column and use np.select to assign values to it using our lists as arguments
df1['Type'] = np.select(conditions, values)

df1


# In[ ]:




