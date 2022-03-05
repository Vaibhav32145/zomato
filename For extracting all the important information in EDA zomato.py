#!/usr/bin/env python
# coding: utf-8

# ## Zomato Exploring data analysis and feature engineering

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[3]:


df.columns


# In[4]:


df.info()                   #Cateogorical variable, integer variable or text data


# In[5]:


df.describe()


# ## IN DATA ANALYSIS What all things we do-:
# ### Missing values
# ### Explore about the numerical variable
# ### Explore about the categorical variable
# ### finding relationship between features

# In[6]:


df.isnull().sum()


# In[7]:


#Another way to find out missing values

[features for features in df.columns if df[features].isnull().sum()>0]


# In[8]:


df.shape


# In[9]:


sns.heatmap(df.isnull(),yticklabels=False, cbar=False, cmap='viridis')   #Due to many no. of rows we can't see the missing value


# In[10]:


df_country=pd.read_excel('Country-code.xlsx')
df_country.head()


# In[11]:


df.columns


# In[12]:


final_df=pd.merge(df,df_country,on='Country Code', how='left')                    # for combining two dataframe


# In[13]:


final_df.head(2)


# In[14]:


# to check datatype
final_df.dtypes


# In[15]:


final_df.columns


# In[16]:


country_names=final_df.Country.value_counts().index   #Which we can understand that Zomato's maximum business grow in India


# In[17]:


country_val=final_df.Country.value_counts().values


# In[18]:


## Pie chart
plt.pie(x=country_val,labels=country_names)


# In[19]:


#Above plot is really bad so it's jumbled
#top 3 country that uses zomato
## Pie chart
plt.pie(x=country_val[:3],labels=country_names[:3], autopct='%1.2f%%')       # confusion-%1.2f%% what it is


# Observation: Zomato maximum records or transaction are from India, USA, UK respectively.

# In[20]:


final_df.columns


# In[21]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[22]:


ratings


# ## Observation
# #### When Ratings is between 4.5 to 4.9---->Excellent
# #### When the Ratings are between 4.0 to 3.4 ----> Very Good
# #### When the Ratings are between 3.5 to 3.9 -----> good
# #### When the Ratings are between 3.0 to 3.4 -----> Average
# #### When the Ratings are between 2.5 to 2.9 -----> good
# #### When the Ratings are between 2.0to 2.4 -----> poor

# In[23]:


ratings.head()


# In[24]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,16)
sns.barplot(x="Aggregate rating",y="Rating Count", data=ratings)


# In[25]:


sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color', data=ratings, palette=['blue','red','orange','yellow','green','green'])


# ### Observation:
# ##### 1- Not rated count is very high.
#  ##### 2- maximum number of rating are between 2.5 to 3.4

# In[26]:


## Countplot
sns.countplot(x="Rating color",data=ratings,palette=['blue','red','orange','yellow','green','green'])


# In[27]:


ratings


# In[32]:


## Find the country name that has given 0 rating.
final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# In[37]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)  #2nd way to see 0 rating


# ### Observation-
# ##### 1-Maimum number of 0 ratings are from Indian customers

# In[35]:


# find out which currency is used by which country?
final_df.columns


# In[43]:


final_df.groupby(['Country','Currency']).size().reset_index()


# In[45]:


## Which country do have online delivery option
final_df.groupby(['Has Online delivery','Country']).size().reset_index()


# #### Observation:
# ###### 1-Online delieveries are available in India and UAE

# In[46]:


## Create a piechart for cities distribution
final_df.columns


# In[51]:


city_val=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index


# In[54]:


plt.pie(x=city_val[:5],labels=city_labels[:5], autopct='%1.2f%%')


# In[ ]:


## assignment top 10 cuisine


# In[ ]:





# In[ ]:





# In[ ]:




