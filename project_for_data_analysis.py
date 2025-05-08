# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

file_path = r"C:\Users\Asus\OneDrive\Desktop\data analysis\practice data\Sample - Superstore.csv"

# Try reading with ISO-8859-1 encoding to avoid UnicodeDecodeError
df = pd.read_csv(file_path, encoding='ISO-8859-1')

print(df.head())

print(df.shape)         # Rows and columns
print(df.columns)       # Column names
print(df.info())        # Data types and nulls
print(df.describe())    # Summary stats for numeric columns



import matplotlib.pyplot as plt

# Group by category
category_sales = df.groupby('Category')['Sales'].sum()

# Plot
category_sales.plot(kind='bar', title='Total Sales by Category')
plt.ylabel('Sales')
plt.show()

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

monthly_sales = df.resample('M', on='Order Date')['Sales'].sum()

monthly_sales.plot(title='Monthly Sales Over Time')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.show()

category_profit = df.groupby('Category')['Profit'].sum()
category_profit.plot(kind='bar', title='Total Profit by Category', color='green')
plt.ylabel('Profit')
plt.show()
discount_impact = df.groupby('Discount')['Profit'].mean()
discount_impact.plot(title='Average Profit at Different Discount Levels')
plt.xlabel('Discount')
plt.ylabel('Average Profit')
plt.show()
city_profit = df.groupby('City')['Profit'].sum().sort_values(ascending=False)

# Top 10 profitable cities
city_profit.head(10).plot(kind='bar', title='Top 10 Cities by Profit', color='blue')
plt.ylabel('Profit')
plt.show()

# Bottom 10 cities (losses)
city_profit.tail(10).plot(kind='bar', title='Bottom 10 Cities by Profit (Losses)', color='red')
plt.ylabel('Profit')
plt.show()
segment_profit = df.groupby('Segment')['Profit'].sum()
region_profit = df.groupby('Region')['Profit'].sum()

segment_profit.plot(kind='pie', autopct='%1.1f%%', title='Profit by Segment')
plt.ylabel('')
plt.show()

region_profit.plot(kind='bar', title='Profit by Region')
plt.ylabel('Profit')
plt.show()

subcat_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values()
subcat_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values()

subcat_sales.plot(kind='barh', title='Sales by Sub-Category')
plt.xlabel('Sales')
plt.show()

subcat_profit.plot(kind='barh', title='Profit by Sub-Category', color='orange')
plt.xlabel('Profit')
plt.show()
