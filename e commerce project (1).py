#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio. templates.default = "plotly_white"


# In[2]:


data = pd.read_csv("Sample - Superstore.csv", encoding = 'latin-1 ')


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.describe()


# In[6]:


data.info()


# # converting date columns

# In[7]:


data['Order Date'] = pd.to_datetime(data['Order Date']) 
data['Ship Date'] = pd.to_datetime(data['Ship Date'])
 


# In[8]:


data.head()


# In[9]:


data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Day of Week'] = data['Order Date'].dt.dayofweek


# In[10]:


data.head()


# # Monthly sales analysis

# In[11]:


sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()


# In[12]:


sales_by_month


# In[13]:


fig = px.line(sales_by_month,
               x='Order Month',
               y='Sales',
               title='Monthly Sales Analysis')
fig.show()


# In[14]:


data.head()


#  Sales by Category

# In[15]:


sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()


# In[16]:


sales_by_category


# In[17]:


fig = px.pie(sales_by_category,
            values = 'Sales',
            names ='Category',
            hole = 0.05,
            color_discrete_sequence = px.colors.qualitative.Pastel)

fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
fig.update_layout(title_text = 'Sales Analysis by Category', title_font = dict(size=24))

fig.show()


# # Sales analysis by sub Category

# In[18]:


data.head()


# In[19]:


sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()


# In[20]:


sales_by_subcategory


# In[21]:


fig = px.bar(sales_by_subcategory, x= 'Sub-Category', y= 'Sales', title = "Sales analysis by sub category")
fig.show()


# # Monthly profit analysis

# In[22]:


profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()


# In[23]:


profit_by_month


# In[24]:


fig = px.line(profit_by_month, x='Order Month', y= 'Profit', title= 'Monthly profit analysis')
fig.show()


# # profit by category

# In[25]:


profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()


# In[26]:


profit_by_category


# In[27]:


fig = px.pie(profit_by_category,
            values = 'Profit',
            names= 'Category',
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo= 'percent+label')
fig.update_layout(title_text= 'Profit Analysis by Category',title_font = dict(size=24))

fig.show()


# # profit by sub category
# 

# In[28]:


profit_by_subcategory = data.groupby('Sub-Category')['Profit'].sum().reset_index()
fig = px.bar(profit_by_subcategory, x='Sub-Category',
            y='Profit',
            title='Profit Analysis by Sub-Category')
fig.show()


# # sales and profit - customer segment 

# In[29]:


data.head()


# In[30]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()

color_palette = colors.qualitative.Pastel

fig = go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                     y=sales_profit_by_segment['Sales'],
                     name='Sales',
                     marker_color=color_palette[0]))
              
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                     y=sales_profit_by_segment['Profit'],
                     name='Profit',
                     marker_color=color_palette[1])) 
fig.update_layout(title= 'Sales and Profit analysis by Customer Segment',
                 xaxis_title='Customer Segment',yaxis_title='Amount')
fig.show()


# # sales to profit ratio

# In[31]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio'] = sales_profit_by_segment['Sales']/sales_profit_by_segment['Profit']
print(sales_profit_by_segment[['Segment','Sales_to_Profit_Ratio']])


# In[ ]:





# In[ ]:




