import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# Run SQL query to get total quantity sold and total revenue
query = """
SELECT 
    SUM(quantity) AS total_quantity_sold, 
    SUM(quantity * price) AS total_revenue 
FROM sales
"""
df = pd.read_sql_query(query, conn)
conn.close()

# Extract values
total_quantity_sold = df['total_quantity_sold'][0]
total_revenue = df['total_revenue'][0]

# Print the results
print("=== Basic Sales Summary ===")
print(f"Total Quantity Sold: {total_quantity_sold}")
print(f"Total Revenue: ${total_revenue:.2f}")

# Plot the summary as a bar chart
df.T.plot(kind='bar', legend=False, color=['green'])
plt.title("Total Sales Summary")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()

# Save the chart
plt.savefig("total_sales_summary_chart.png")
plt.show()
