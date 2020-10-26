#!/usr/bin/env python
# coding: utf-8

# # Netflix Viewing History Analysis for Moro

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mlt
import numpy as np
from scipy import stats
import datetime
sns.set


# ### Just a fun project to find out what Moro spends her time on while on Netflix. Does she prefer movies to TV shows, does she spend time every day of the week watching stuff? What month did she watch the most stuff on Netflix and what particular show is she really into?

# In[2]:


# Read in files and print the information
# NetflixViewingHistory.csv was downloaded from Netflix from Viewer's activity. 
df= pd.read_csv('/Users/nae/Desktop/Dublin Business School/NetflixViewingHistoryMORO.csv')


# In[3]:


#View top 10 rows 
df.head(10)


# In[4]:


#View bottom 10 rows 
df.tail(10)


# In[5]:


df['Date'] = pd.to_datetime(df['Date'])
df['Year'], df['Month'] = df['Date'].dt.year, df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day
df['Day_of_week'] = df['Date'].dt.day_name()


# In[6]:


show_details = df.Title.str.split(":",expand=True,n=2)
#show_details
df['show_name'] = show_details[0]
df['season'] = show_details[1]
df['episode_name'] = show_details[2]


# In[7]:


#If the season column is "None" them it is most likely a movie, lets add another column to our dataframe 
#my_history[my_history['season'].isna()]
df['show_type'] = df.apply(lambda x:'Movie' if pd.isnull(x['season']) else 'TV Show' , axis=1)
df


# In[ ]:





# In[8]:


plt.figure(figsize = (12, 8)) 
sns.countplot(x = 'show_type', data = df)


# ### Moro watches to a significant level, more tv shows than movies. 

# In[9]:


plt.figure(figsize = (18, 10)) 
sns.countplot(y = 'show_name', data = df, order=df['show_name'].value_counts().iloc[:10].index)


# ### I thought 'Friends' would be taking the lead, but look at that... Moro must really love Fresh Princes ;)

# In[10]:


plt.figure(figsize = (12, 8)) 
sns.countplot(x = 'Day_of_week', data = df)


# #### Well, Moro seems to prefer watching stuff on Saturdays and Sundays which isn't so bad. I mean, thats pretty normal, isn't it?

# In[11]:



plt.figure(figsize = (12, 8)) 
sns.countplot(x = 'Month', data = df)


# #### LOL! MARCH!!!  Look at that Spike... To be fair, Moro went on vacation in March, lockdown was happening in March due to Covid19... There's another reason for the spike but that's between us. Lol

# In[12]:


plt.figure(figsize = (12, 8))
ax=sns.heatmap(data=df.corr(), annot = True, cmap='seismic_r')


# In[ ]:




