#!/usr/bin/env python
# coding: utf-8

# Project Scope:
# Contains data for six different countries, covering years from 2000 to 2015. There no do appear to be significant data anamolies based on initial inspection of the file. GDP data is in scientific format.
# 
# 1) Will be comparing changes between the countries, in their GDP and life expectancy, over the span of years in the dataset.
# 2) Will be looking to see changes in life expectancy correlate to changes to GDP, and how so. Do they move up/down together? Or does one go up while the other down?
# 3) Will gather information on the max, min, mean, other summarical data for each country regarding their GDP and life expectancy.
# 4) No information is given to what portion of a country's GDP is used for medical expenditures (i.e., treatment, research, subsidies, etc.).
# 5) Very focued and limited data, does not account for many other variables that may affect life expectancy positively or negatively.
# 

# In[1]:


#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#import csv file
all_data = pd.read_csv("all_data.csv")


# In[3]:


print(all_data.head())
print(all_data.describe())


# In[4]:


#convert GDP data to a more usable format
all_data["GDP_value"] = all_data["GDP"] / 1000000000

print(all_data.head())


# In[5]:


#f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.lineplot(
    data=all_data
    , x="Year"
    , y="Life expectancy at birth (years)"
    , hue="Country"
#    , ax=axs[0]
)

plt.show()
plt.clf()

sns.lineplot(
    data=all_data
    , x="Year"
    , y="GDP_value"
    , hue="Country"
#    , ax=axs[1]
)
#f.tight_layout()

plt.show()
plt.clf()


# In[13]:


#separate dictionary for Chile
chile_data = all_data[all_data.Country == 'Chile']

#separate dictionary for China
china_data = all_data[all_data.Country == 'China']

#separate dictionary for Germany
germany_data = all_data[all_data.Country == 'Germany']

#separate dictionary for Mexico
mexico_data = all_data[all_data.Country == 'Mexico']

#separate dictionary for United States of America
usa_data = all_data[all_data.Country == 'United States of America']

#separate dictionary for Zimbabwe
zimbabwe_data = all_data[all_data.Country == 'Zimbabwe']


# In[9]:


#data visualations for Chile
f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.lineplot(
    data=chile_data
    , x="Year"
    , y="Life expectancy at birth (years)"
#    , hue="Country"
    , ax=axs[0]
)
sns.lineplot(
    data=chile_data
    , x="Year"
    , y="GDP_value"
#    , hue="Country"
    , ax=axs[1]
)
f.tight_layout()

plt.show()
plt.clf()


# In[11]:


sns.scatterplot(data=chile_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()


# In[12]:


sns.lmplot(data=chile_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()


# In[21]:


#data visualations for China
f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.lineplot(
    data=china_data
    , x="Year"
    , y="Life expectancy at birth (years)"
    , ax=axs[0]
)
sns.lineplot(
    data=china_data
    , x="Year"
    , y="GDP_value"
    , ax=axs[1]
)
f.tight_layout()

plt.show()
plt.clf()


sns.scatterplot(data=china_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()

sns.lmplot(data=china_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()


# In[17]:


#data visualations for Germany
f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.lineplot(
    data=germany_data
    , x="Year"
    , y="Life expectancy at birth (years)"
    , ax=axs[0]
)
sns.lineplot(
    data=germany_data
    , x="Year"
    , y="GDP_value"
    , ax=axs[1]
)
f.tight_layout()

plt.show()
plt.clf()


sns.scatterplot(data=germany_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()

sns.lmplot(data=germany_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()


# In[18]:


#data visualations for Mexico
f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.lineplot(
    data=mexico_data
    , x="Year"
    , y="Life expectancy at birth (years)"
    , ax=axs[0]
)
sns.lineplot(
    data=mexico_data
    , x="Year"
    , y="GDP_value"
    , ax=axs[1]
)
f.tight_layout()

plt.show()
plt.clf()


sns.scatterplot(data=mexico_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()

sns.lmplot(data=mexico_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()


# In[19]:


#data visualations for United States of America
f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.lineplot(
    data=usa_data
    , x="Year"
    , y="Life expectancy at birth (years)"
    , ax=axs[0]
)
sns.lineplot(
    data=usa_data
    , x="Year"
    , y="GDP_value"
    , ax=axs[1]
)
f.tight_layout()

plt.show()
plt.clf()


sns.scatterplot(data=usa_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()

sns.lmplot(data=usa_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()


# In[20]:


#data visualations for Zimbabwe
f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.lineplot(
    data=zimbabwe_data
    , x="Year"
    , y="Life expectancy at birth (years)"
    , ax=axs[0]
)
sns.lineplot(
    data=zimbabwe_data
    , x="Year"
    , y="GDP_value"
    , ax=axs[1]
)
f.tight_layout()

plt.show()
plt.clf()


sns.scatterplot(data=zimbabwe_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()

sns.lmplot(data=zimbabwe_data, x="Life expectancy at birth (years)", y="GDP_value")

plt.show()
plt.clf()


# In[ ]:




