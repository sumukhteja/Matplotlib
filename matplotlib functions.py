#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_path = "C:/Users/sunny/Downloads/sales_data.csv"
df = data = pd.read_csv("C:/Users/sunny/Downloads/sales_data.csv", encoding="latin1")

# Line plot
plt.plot(df['ORDERDATE'], df['SALES'])
plt.title('Sales over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Scatter plot
plt.scatter(df['QUANTITYORDERED'], df['PRODUCTLINE'])
plt.title('Quantity Ordered vs. Product Line')
plt.xlabel('Quantity Ordered')
plt.ylabel('Product Line')
plt.show()

# Vertical bar plot
plt.bar(df['PRODUCTLINE'], df['SALES'])
plt.title('Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Sales')
plt.xticks(rotation=90)
plt.show()

# Horizontal bar plot
plt.barh(df['PRODUCTLINE'], df['SALES'])
plt.title('Sales by Product Line')
plt.xlabel('Sales')
plt.ylabel('Product Line')
plt.show()

# Histogram
plt.hist(df['SALES'], bins=10)
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# Box plot
plt.boxplot(df['SALES'])
plt.title('Sales Distribution')
plt.ylabel('Sales')
plt.show()

# Pie chart
plt.pie(df['SALES'], labels=df['PRODUCTLINE'], autopct='%1.1f%%')
plt.title('Sales by Product Line')
plt.show()

# Error bars
x = df['PRODUCTLINE']
y = df['SALES']
error = [0.1 * s for s in y]  # Example error values, adjust as needed
plt.errorbar(x, y, yerr=error, fmt='o')
plt.title('Sales with Error Bars')
plt.xlabel('Product Line')
plt.ylabel('Sales')
plt.show()

# Area plot
plt.stackplot(df['ORDERDATE'], df['SALES'], labels=df['PRODUCTLINE'])
plt.title('Sales by Product Line over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.show()

# Grouped bar plot
grouped_df = df.groupby('PRODUCTLINE')['SALES'].sum().reset_index()
plt.bar(grouped_df['PRODUCTLINE'], grouped_df['SALES'])
plt.title('Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=90)
plt.show()

# Scatter plot with color mapping
plt.scatter(df['QUANTITYORDERED'], df['PRICEEACH'], c=df['SALES'], cmap='viridis')
plt.title('Quantity Ordered vs. Price Each')
plt.xlabel('Quantity Ordered')
plt.ylabel('Price Each')
plt.colorbar(label='Sales')
plt.show()

# Stacked bar plot
stacked_df = df.groupby('YEAR_ID')[['SALES']].sum().reset_index()
plt.bar(stacked_df['YEAR_ID'], stacked_df['SALES'], label='Sales')
plt.bar(stacked_df['YEAR_ID'], stacked_df['QUANTITYORDERED'], label='Quantity Ordered')
plt.title('Sales and Quantity Ordered by Year')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()

# Heatmap
heatmap_df = df.pivot_table(index='YEAR_ID', columns='MONTH_ID', values='SALES', aggfunc='sum')
plt.imshow(heatmap_df, cmap='hot', interpolation='nearest')
plt.title('Monthly Sales Heatmap')
plt.xlabel('Month')
plt.ylabel('Year')
plt.colorbar(label='Sales')
plt.show()

# Violin plot
plt.violinplot(df['SALES'], vert=False)
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.show()

# Pairwise scatter plot
pd.plotting.scatter_matrix(df[['QUANTITYORDERED', 'PRICEEACH', 'SALES']], figsize=(8, 8))
plt.suptitle('Pairwise Scatter Plot')
plt.show()

# Stacked area plot
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
df_sorted = df.sort_values(by='ORDERDATE')
plt.stackplot(df_sorted['ORDERDATE'], df_sorted['SALES'], labels=df_sorted['PRODUCTLINE'])
plt.title('Sales by Product Line over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.show()

# Donut/pie chart
sales_by_productline = df.groupby('PRODUCTLINE')['SALES'].sum()
plt.pie(sales_by_productline, labels=sales_by_productline.index, autopct='%1.1f%%', wedgeprops={'width': 0.4})
plt.title('Sales Distribution by Product Line')
plt.show()

# Word cloud
from wordcloud import WordCloud
text = ' '.join(df['PRODUCTLINE'])
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Product Line')
plt.show()

# Area plot
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
df_sorted = df.sort_values(by='ORDERDATE')
plt.fill_between(df_sorted['ORDERDATE'], df_sorted['SALES'])
plt.title('Sales over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Heatmap
import seaborn as sns

corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Grouped bar plot
sales_by_productline = df.groupby('PRODUCTLINE')['SALES'].sum()
sales_by_territory = df.groupby('TERRITORY')['SALES'].sum()

fig, ax = plt.subplots(2, 1, figsize=(8, 8))
ax[0].bar(sales_by_productline.index, sales_by_productline)
ax[0].set_title('Sales by Product Line')
ax[0].set_xlabel('Product Line')
ax[0].set_ylabel('Sales')

ax[1].bar(sales_by_territory.index, sales_by_territory)
ax[1].set_title('Sales by Territory')
ax[1].set_xlabel('Territory')
ax[1].set_ylabel('Sales')

plt.tight_layout()
plt.show()

# Treemap
import squarify

sales_by_country = df.groupby('COUNTRY')['SALES'].sum().reset_index()

plt.figure(figsize=(10, 6))
squarify.plot(sizes=sales_by_country['SALES'], label=sales_by_country['COUNTRY'], alpha=0.8)
plt.axis('off')
plt.title('Sales by Country')
plt.show()


# In[ ]:




