#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[18]:


df_tracks= pd.read_csv("/Users/madhav/Study/SpotifyDataAnalysis/archive/tracks.csv")
df_tracks.head()


# In[19]:


#Checking null conditions

pd.isnull(df_tracks).sum()


# In[20]:


df_tracks.info()


# In[21]:


#Least popular songs
sorted_df= df_tracks.sort_values('popularity', ascending = True).head(10)
sorted_df


# In[22]:


#descriptive statatics
df_tracks.describe().transpose()


# In[10]:


#top 10 songs
most_popular =df_tracks.query('popularity > 90' , inplace = False).sort_values('popularity',ascending = False)
most_popular[:10]


# In[24]:


df_tracks.set_index('release_date', inplace = True)
df_tracks.index=pd.to_datetime(df_tracks.index)
df_tracks.head()


# In[27]:


#artist in specific row
df_tracks[['artists']].iloc[18]


# In[28]:


df_tracks['duration'] = df_tracks['duration_ms'].apply(lambda x: round(x/1000))
df_tracks.drop('duration_ms', inplace = True, axis =1)


# In[29]:


df_tracks.duration.head()


# In[31]:


#Correlation map
corr_df = df_tracks.drop(['key', 'mode', 'explicit'],axis = 1).corr(method = 'pearson')
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df, annot = True, fmt ='.1g', vmin = -1, vmax = 1, center = 0, cmap = 'inferno', linewidths = 1, linecolor = 'Black')
heatmap.set_title('Correlation HeatMap Between Variable')
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation = 90)


# In[33]:


sample_df = df_tracks.sample(int(0.004*len(df_tracks)))


# In[34]:


print(len(sample_df))


# In[35]:


plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y = 'loudness', x = 'energy', color = 'c').set(title = 'Loudness VS Energy Coorealtion')


# In[37]:


plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y = 'popularity', x = 'acousticness', color = 'b').set(title = 'Popularity VS Acouticness Coorealtion')


# In[41]:


df_tracks['dates'] = df_tracks.index.get_level_values('release_date')
df_tracks.dates = pd.to_datetime(df_tracks.dates)
years = df_tracks.dates.dt.year


# In[42]:


sns.displot(years, discrete = True, aspect = 2, height = 5, kind = 'hist').set(title = 'Number of songs per year')


# In[43]:


#bar plot
total_dr = df_tracks.duration
fig_dims = (18,7)
fig, ax = plt.subplots(figsize = fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax = ax, errwidth = False).set(title = 'Year VS Duration')
plt.xticks(rotation=90)


# In[46]:


#Line plot
total_dr = df_tracks.duration
sns.set_style(style='whitegrid')
fig_dims = (10, 5)
fig, ax = plt.subplots(figsize = fig_dims)
fig = sns.lineplot(x = years, y = total_dr, ax = ax).set(title = 'Year VS Duration')
plt.xticks(rotation=60)


# In[47]:


df_genre = pd.read_csv('/Users/madhav/Study/SpotifyDataAnalysis/SpotifyFeatures.csv')


# In[48]:


df_genre.head()


# In[49]:


plt.title('Duration of the Songs in Different Genres')
sns.color_palette('rocket', as_cmap = True)
sns.barplot(y= 'genre', x ='duration_ms', data = df_genre)
plt.xlabel('Duration in millisecons')
plt.ylabel('Genres')


# In[50]:


sns.set_style(style="darkgrid")
plt.figure(figsize = (10,5))
famous= df_genre.sort_values("popularity", ascending = False).head(10)
sns.barplot(y= 'genre' , x ='popularity', data = famous).set(title = 'Top 5 Genres by Popularity')


# In[ ]:




