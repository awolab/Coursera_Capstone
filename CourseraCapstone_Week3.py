#!/usr/bin/env python
# coding: utf-8

# # Capstone Project Notebook
# This notebook will be mainly used for the capstone project.

# ## WEEK 3
# 1. Create a new Notebook for this assignment.
# 2. Create the dataframe:
# * The dataframe will consist of three columns: PostalCode, Borough, and Neighborhood
# * Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned.
# * More than one neighborhood can exist in one postal code area. For example, in the table on the Wikipedia page, you will notice that M5A is listed twice and has two neighborhoods: Harbourfront and Regent Park. These  two rows will be combined into one row with the neighborhoods separated with a comma as shown in row 11  in the above table.
# * If a cell has a borough but a Not assigned  neighborhood, then the neighborhood will be the same as the borough.
#  Clean your Notebook and add Markdown cells to explain your work and any assumptions you are making.
# * In the last cell of your notebook, use the .shape method to print the number of rows of your dataframe.

# In[22]:


#Let's download all the dependencies that we will need

import pandas as pd
import html5lib 

#Import data from wikipedia
data=pd.read_html('https://en.wikipedia.org/w/index.php?title=List_of_postal_codes_of_Canada:_M&oldid=1011037969',skiprows=0)[0]
df=data

#THIS IS ANOTHER METHOD USING BEAUTIFUL SOUP - IT WORKS TOO!
#We first have to import the library, and create an instance of the BeautifulSoup class to parse our document:
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(page.content, 'html.parser')
#from bs4 import BeautifulSoup
#path_wiki=requests.get("https://en.wikipedia.org/w/index.php?title=List_of_postal_codes_of_Canada:_M&oldid=1011037969").text
#soup=BeautifulSoup(path_wiki,'lxml')
#print(soup.title)
#from IPython.display import display_html
#tabla = str(soup.table)
#display_html(tabla,raw=True)

# Rename 'Postal Code' column to 'PostalCode'
df.rename(columns = {'Postal Code':'PostalCode'}, inplace = True)
df.shape
df.head(20)


# In[28]:


#Ignore cells with a borough that is Not assigned.
df.drop(df.index[df['Borough'] == 'Not assigned'], inplace = True)

# Reset index column
df.reset_index(drop=True)


# In[29]:


# Check number of rows and columns
df.shape 


# In[ ]:




