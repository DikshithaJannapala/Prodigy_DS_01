#!/usr/bin/env python
# coding: utf-8

# # Prodigy Infotech Project task 1
# Problem Statment :
# Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"C:\Users\ADMIN\Downloads\World population(1) - Copy.csv")


# In[3]:


data


# In[4]:


# shape check
data.shape


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.isna().sum()


# In[8]:


# Drop unuseful columns
data.drop(columns=['Country Code','Indicator Name'],inplace=True)


# In[9]:


# filter data for total population
total_population_data=data[data['Indicator Code']=='SP.POP.TOTL']
total_population_data


# In[10]:


# sort data based on total population for 2022
total_population_sort = total_population_data.sort_values(by='2022',ascending=False)
total_population_sort


# # Top 10 Countries with highest population in 2022

# In[11]:


top_ten_countries = total_population_sort.head(10)
print("Top Ten Counteies Of Total Population:-")
print(top_ten_countries)


# # Data visualization

# # Top 10 Countries with highest population in year 2022 and 2000

# In[33]:


# creat a bar plot
plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="black"

plt.subplot(2,2,1)
plot=sns.barplot(x='2022',y="Country Name",data=top_ten_countries)
plt.title("Top Ten countries Of Total Population (2022)")
plt.xlabel("Total population")
plt.ylabel("country")


plt.subplot(2,2,2)
plot=sns.barplot(x='2000',y="Country Name",data=top_ten_countries)
plt.title("Top Ten countries Of Total Population in 2000")
plt.xlabel("Total population")
plt.ylabel("country")


# # Top 10 Countries with highest population in year 1999 and 1978

# In[38]:


# creat a bar plot
plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="black"

plt.subplot(2,2,1)
plot=sns.barplot(x='1999',y="Country Name",data=top_ten_countries)
plt.title("Top Ten countries Of Total Population (1999)")
plt.xlabel("Total population")
plt.ylabel("country")


plt.subplot(2,2,2)
plot=sns.barplot(x='1978',y="Country Name",data=top_ten_countries)
plt.title("Top Ten countries Of Total Population in 1978")
plt.xlabel("Total population")
plt.ylabel("country")


# # Top 10 Countries with highest population in year 1960 and 1968

# In[39]:


# creat a bar plot
plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="black"

plt.subplot(2,2,1)
plot=sns.barplot(x='1960',y="Country Name",data=top_ten_countries)
plt.title("Top Ten countries Of Total Population (1960)")
plt.xlabel("Total population")
plt.ylabel("country")


plt.subplot(2,2,2)
plot=sns.barplot(x='1968',y="Country Name",data=top_ten_countries)
plt.title("Top Ten countries Of Total Population in 1968")
plt.xlabel("Total population")
plt.ylabel("country")


# # Bottom 10 countries with the highest population

# In[15]:


total_population_sort_bot = total_population_data.sort_values(by='2022',ascending=True)
total_population_sort_bot


# In[17]:


top_ten_bot_countries = total_population_sort_bot.head(10)
print("Top Ten Bottom Counteies Of Total Population:-")
print(top_ten_bot_countries)


# # Bottom top 10 Countries with highest population in year 2022 and 2000

# In[37]:


# creat a bar plot
plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="black"

plt.subplot(2,2,1)
plot=sns.barplot(x='2022',y="Country Name",data=top_ten_bot_countries)
plt.title("Top Ten Bottom countries Of Total Population (2022)")
plt.xlabel("Total population")
plt.ylabel("country")


plt.subplot(2,2,2)
plot=sns.barplot(x='2000',y="Country Name",data=top_ten_bot_countries)
plt.title("Top Ten Bottom countries Of Total Population in 2000")
plt.xlabel("Total population")
plt.ylabel("country")


# # Bottom top 10 Countries with highest population in year 1999 and 1989

# In[36]:


# creat a bar plot
plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="black"

plt.subplot(2,2,1)
plot=sns.barplot(x='1999',y="Country Name",data=top_ten_bot_countries)
plt.title("Top Ten Bottom countries Of Total Population (1999)")
plt.xlabel("Total population")
plt.ylabel("country")


plt.subplot(2,2,2)
plot=sns.barplot(x='1989',y="Country Name",data=top_ten_bot_countries)
plt.title("Top Ten Bottom countries Of Total Population in 1989")
plt.xlabel("Total population")
plt.ylabel("country")


# # Bottom top 10 Countries with highest population in year 1960 and 1968

# In[41]:


# creat a bar plot
plt.figure(figsize=(20,13))
plt.rcParams['axes.facecolor']=="black"

plt.subplot(2,2,1)
plot=sns.barplot(x='1960',y="Country Name",data=top_ten_bot_countries)
plt.title("Top Ten Bottom countries Of Total Population (1960)")
plt.xlabel("Total population")
plt.ylabel("country")


plt.subplot(2,2,2)
plot=sns.barplot(x='1968',y="Country Name",data=top_ten_bot_countries)
plt.title("Top Ten Bottom countries Of Total Population in 1968")
plt.xlabel("Total population")
plt.ylabel("country")


plt.tight_layout()


# # Top 10 countries with highest male population
# 

# In[21]:


data.sample(10)


# In[22]:


# filter data for total male population
total_population_male=data[data['Indicator Code']=='SP.POP.TOTL.MA.IN']
total_population_male


# In[23]:


# sort data based on total population in 2022
total_population_sort_male = total_population_male.sort_values(by='2022',ascending=False)
total_population_sort_male


# In[24]:


#top 10 countries with the highest population in 2022
top_ten_male_countries = total_population_sort_male.head(10)
print("Top Ten male Counteies Of Total Population:-")
print(top_ten_male_countries)


# # Top 10 countries with highest female population

# In[25]:


# filter data for total female population
total_population_female=data[data['Indicator Code']=='SP.POP.TOTL.MA.IN']
total_population_female


# In[26]:


# sort data based on total population in 2022
total_population_sort_female = total_population_female.sort_values(by='2022',ascending=False)
total_population_sort_female


# In[27]:


#top 10 countries with the highest population in 2022
top_ten_female_countries = total_population_sort_female.head(10)
print("Top Ten female Counteies Of Total Population:-")
print(top_ten_female_countries)


# In[ ]:




