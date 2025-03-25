import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "data/sales_data_storytelling.csv"
df = pd.read_csv(file_path, parse_dates=['Date'])

# Ensure the Date column is properly formatted
df['Month'] = df['Date'].dt.to_period('M')

# 1. Plot monthly trends in total revenue
monthly_revenue = df.groupby('Month')['Revenue'].sum()
plt.figure(figsize=(10,5))
monthly_revenue.plot(marker='o', linestyle='-')
plt.title('Monthly Revenue Trends')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Identify peak and low-performing months
peak_month = monthly_revenue.idxmax()
low_month = monthly_revenue.idxmin()
print(f"Peak month: {peak_month}, Low month: {low_month}")

# 2. Bar chart of average revenue per product
avg_revenue_per_product = df.groupby('Product')['Revenue'].mean().sort_values(ascending=False)
plt.figure(figsize=(10,5))
avg_revenue_per_product.plot(kind='bar', color='skyblue')
plt.title('Average Revenue per Product')
plt.xlabel('Product')
plt.ylabel('Average Revenue')
plt.xticks(rotation=45)
plt.show()

# Identify best-selling item
best_selling_product = avg_revenue_per_product.idxmax()
print(f"Best-selling product: {best_selling_product}")

# 3. Pie chart showing sales contribution of each product
total_revenue_per_product = df.groupby('Product')['Revenue'].sum()
plt.figure(figsize=(8,8))
total_revenue_per_product.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='Paired')
plt.title('Sales Contribution per Product')
plt.ylabel('')  # Hide y-label
plt.show()

# 4. Detect seasonal patterns or anomalies
plt.figure(figsize=(12,5))
sns.boxplot(x=df['Month'].astype(str), y=df['Revenue'])
plt.title('Revenue Distribution by Month')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

# 5. Prepare a short visual report/story
summary_text = f'''
Business Performance Summary:
- Peak sales month: {peak_month}, indicating strong demand.
- Lowest sales month: {low_month}, requiring investigation into potential causes.
- The best-selling product is '{best_selling_product}', contributing the most revenue.
- Sales distribution suggests possible seasonal trends, requiring further analysis.
- Overall revenue trends and product contributions suggest areas for strategic focus.
'''
print(summary_text)
