#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import glob
import os

pd.options.display.max_columns = 200
pd.options.display.max_rows = 200


# In[47]:


filedir ='C:\\Users\\mlin1\\Box\\Hospital_marketing_EA_data_load\\'


# In[75]:

"""
tb = {}
for filename in os.listdir(filedir):
    for f in glob.glob(filedir+filename):
        if filename.endswith(".txt"):
            headers = pd.read_csv(f,sep= '|', nrows=0).columns.tolist()
            tb[filename] = headers
		elif filename.endwith(".xlsx"):
			headers = pd.read_excel(f).columns.tolist()
"""
tb = {}
for filename in os.listdir(filedir):
	for f in glob.glob(filedir+filename):           
		if filename.endswith(".xlsx"):
			headers = pd.read_excel(f).columns.tolist()
			tb[filename] = headers
		elif filename.endswith(".txt"):
			headers = pd.read_csv(f,sep= '|', nrows=0).columns.tolist()
			tb[filename] = headers
# In[78]:


headers = []
for k,v in tb.items():
    for i in v:
        headers.append([k,i])
        tb = pd.DataFrame(headers, columns = ['FileName','Fields'])       


# In[80]:


tb.to_excel('C:\\Users\\mlin1\\Downloads\\IQVIA_HEADERS_1002.xlsx', index=False)


# In[ ]:




