#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#retrieve remote data file by url
url="http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data" 
data = pd.read_csv(url)
#add column names
data.columns = ["age","workclass","fnlwgt","education","educationnum","maritalstatus","occupation","relationship","race","sex","capitalgain","capitalloss","hoursperweek","nativecountry", "salary"]


# In[3]:


#brief summary of the data file
data.info()


# In[4]:


#preview original data
data.head()


# In[5]:


#modify the datafile by removing columns
data.drop('fnlwgt', inplace=True, axis=1)
data.drop('capitalgain', inplace=True, axis=1)
data.drop('capitalloss', inplace=True, axis=1)
data.drop('educationnum', inplace=True, axis=1)
data.head()


# In[6]:


#convert the file from CSV to JSON, written to local file
json_output = r"C:\Users\Student\Desktop\DS 3002\project1data.json"
output = data.to_json(json_output, indent=1, orient="records")

