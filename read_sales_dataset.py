
import pandas as pd

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# Display the first few rows of the dataset
print("=== Sales Dataset Preview ===")
print(df.head())

# Display basic summary statistics
print("\n=== Basic Summary ===")
print(df.describe(include='all'))

# Display total quantity and total revenue
df['revenue'] = df['quantity'] * df['price']
total_quantity = df['quantity'].sum()
total_revenue = df['revenue'].sum()

print(f"\nTotal Quantity Sold: {total_quantity}")
print(f"Total Revenue: ${total_revenue:.2f}")
