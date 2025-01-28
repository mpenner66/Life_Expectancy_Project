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

# In[84]:


#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import pearsonr
np.set_printoptions(suppress=True, precision = 1)


# In[85]:


#import csv file
all_data = pd.read_csv("all_data.csv")


# In[86]:


print(all_data.head())
print(all_data.describe())
    
years = range(len(all_data['Year'].unique()))
print(years)
years_label = all_data['Year'].unique()
print(years_label)


# In[87]:


#convert GDP data to a more usable format
all_data["GDP_value"] = all_data["GDP"] / 1000000000

print(all_data.head())


# In[88]:


#f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.lineplot(
    data=all_data
    , x="Year"
    , y="Life expectancy at birth (years)"
    , hue="Country"
#    , ax=axs[0]
)
plt.xticks(rotation=40)
ax = plt.subplot()
ax.set_xticks(years_label)
ax.set_xticklabels(years_label)

plt.show()
plt.clf()


sns.lineplot(
    data=all_data
    , x="Year"
    , y="GDP_value"
    , hue="Country"
#    , ax=axs[1]
)
plt.ylabel("GDP (in billions)")
plt.xticks(rotation=40)
ax = plt.subplot()
ax.set_xticks(years_label)
ax.set_xticklabels(years_label)

plt.show()
plt.clf()

sns.displot(data=all_data, x="Life expectancy at birth (years)", hue="Country", col="Country")

plt.show()
plt.clf()

sns.displot(data=all_data, x="GDP_value", hue="Country", col="Country")

plt.show()
plt.clf()


sns.histplot(
    data=all_data
    , x="Life expectancy at birth (years)"
    , hue="Country"
)

plt.show()
plt.clf()


sns.histplot(
    data=all_data
    , x="GDP_value"
    , hue="Country"
)

plt.show()
plt.clf()


# In[91]:


# #separate dictionary for Chile
# chile_data = all_data[all_data.Country == 'Chile']

# #separate dictionary for China
# china_data = all_data[all_data.Country == 'China']

# #separate dictionary for Germany
# germany_data = all_data[all_data.Country == 'Germany']

# #separate dictionary for Mexico
# mexico_data = all_data[all_data.Country == 'Mexico']

# #separate dictionary for United States of America
# usa_data = all_data[all_data.Country == 'United States of America']

# #separate dictionary for Zimbabwe
# zimbabwe_data = all_data[all_data.Country == 'Zimbabwe']


# In[92]:


agg_data = all_data.reindex(columns=["Country", "Life expectancy at birth (years)", "GDP_value"])

print(
    agg_data.groupby("Country")
    .agg(["mean", "std", "var"])
    )
grouped = agg_data.groupby("Country").mean()


life_gdp_cov = np.cov(grouped["Life expectancy at birth (years)"], grouped["GDP_value"])
print(life_gdp_cov)

life_gdp_cor, p = pearsonr(grouped["Life expectancy at birth (years)"], grouped["GDP_value"])
print(life_gdp_cor)

#Scatterplot for average GDP against Life expetancy
sns.scatterplot(data=grouped, x="Life expectancy at birth (years)", y="GDP_value")
plt.ylabel("GDP (in billions)")

plt.show()
plt.clf()

#Scatterplot with line
sns.lmplot(data=grouped, x="Life expectancy at birth (years)", y="GDP_value")
plt.ylabel("GDP (in billions)")

plt.show()
plt.clf()


# In[77]:


countries = all_data['Country'].unique()

for country in countries:
    country_data = all_data[all_data.Country == country]
    print(country + " had an average GDP (in billions) from 2000-2015 of", np.mean(country_data["GDP_value"]))
    print(country + " had an average life expectancy from 2000-2015 of", np.mean(country_data["Life expectancy at birth (years)"]))

    # # median
    # print(country + " had a median GDP (in billions) from 2000-2015 of", np.median(country_data["GDP_value"]))
    
    # # range
    # print(country + " had a range of GDP (in billions) from 2000-2015 of", np.max(country_data["GDP_value"]) - np.min(country_data["GDP_value"]))
   
    # # interquartile range
    # print(country + " had an interquartile range of GDP (in billions) from 2000-2015 of", np.percentile(country_data["GDP_value"], 75) - np.percentile(country_data["GDP_value"], 25))
    
    # # variance
    # print(country + " had a variance in GDP (in billions) from 2000-2015 of", np.var(country_data["GDP_value"]))
    
    # # standard deviation
    # print(country + " had a standard deviation of GDP (in billions) from 2000-2015 of", np.std(country_data["GDP_value"]))

    life_gdp_cov = np.cov(country_data["Life expectancy at birth (years)"], country_data["GDP_value"])
    print(life_gdp_cov)

    life_gdp_cor, p = pearsonr(country_data["Life expectancy at birth (years)"], country_data["GDP_value"])
    print(life_gdp_cor)

for country in countries:
    country_data = all_data[all_data.Country == country]
    
    #Line graphs for Life expectancy and GDP
    f, axs = plt.subplots(1, 2, figsize=(8, 4)
                         # , gridspec_kw=dict(width_ratios=[4, 3])
                         )
    plt.ylabel("GDP (in billions)")
    plt.xticks(rotation=60)
    
    sns.lineplot(
        data=country_data
        , x="Year"
        , y="Life expectancy at birth (years)"
    #    , hue="Country"
        , ax=axs[0]
    )
    axs[0].set_xticks(years_label)
    axs[0].set_xticklabels(years_label)
    
    plt.title(country)
    sns.lineplot(
        data=country_data
        , x="Year"
        , y="GDP_value"
    #    , hue="Country"
        , ax=axs[1]
    )
    axs[1].set_xticks(years_label)
    axs[1].set_xticklabels(years_label)
    f.tight_layout()
    
    plt.show()
    plt.clf()

    #Scatterplot for GDP against Life expetancy
    sns.scatterplot(data=country_data, x="Life expectancy at birth (years)", y="GDP_value", hue='Year')
    plt.title(country)
    plt.ylabel("GDP (in billions)")
    
    plt.show()
    plt.clf()

    #Scatterplot with line
    sns.lmplot(data=country_data, x="Life expectancy at birth (years)", y="GDP_value")
    plt.ylabel("GDP (in billions)")
    plt.title(country)
    
    plt.show()
    plt.clf()

