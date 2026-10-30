import pandas as pd
import matplotlib.pyplot as plt

# Read Excel
df = pd.read_excel("C:/Users/Admin/Desktop/JYOTI/Food_Dashboard/food_item_performance_data.xlsx")

# Basic calculations
food_sales=df.groupby("Food Item")["Quantity Sold"].sum()
average = food_sales.mean()
highest = food_sales.max()
lowest = food_sales.min()
total_items=df["Food Item"].nunique()
total_quantity=df["Quantity Sold"].sum()

# Create dashboard
fig, ax = plt.subplots(2, 2, figsize=(14, 9))

# 1. Subject-wise marks
food_sales = df.groupby("Food Item")["Quantity Sold"].sum()
ax[0, 0].bar(food_sales.index, food_sales.values)
ax[0, 0].set_title("Food Items Sold")
ax[0, 0].set_xlabel("Food Item")
ax[0, 0].set_ylabel("Quantity Sold")
ax[0, 0].tick_params(axis="x", rotation=30)
# 2. Line graph
daily_sales = df.groupby("Date")["Revenue (₹)"].sum()
daily_sales.index=pd.to_datetime(daily_sales.index)
daily_sales=daily_sales.sort_index()
'''ax[0, 1].plot(daily_sales.index, daily_sales.values, marker="o",label="Daily Revenue")'''
ax[0,1].plot(daily_sales.index,daily_sales.rolling(7,min_periods=1).mean(),linewidth=3,label="7-Day Average")
ax[0, 1].set_title("Daily Revenue Trend")
ax[0, 1].set_xlabel("Date")
ax[0, 1].set_ylabel("Revenue (₹)")
ax[0, 1].tick_params(axis="x", rotation=45)
ax[0, 1].grid(True,alpha=0.3)
# 30. Pie chart
ax[1, 0].pie(
    food_sales.values,
    labels=food_sales.index,
    autopct="%1.1f%%"
)

ax[1, 0].set_title("Quantity sold by food item")
# 4. Summary
ax[1, 1].axis("off")

summary = f"""
FOOD ITEM PERFORMANCE

Average Food Item Sold: {average:.2f}
Highest Food Item Sold: {highest}
Lowest Food Item Sold: {lowest}
Total Unique Food Item: {total_items}
Total Quantity Sold: {total_quantity}
"""

ax[1, 1].text(
    0.1, 0.5,
    summary,
    fontsize=14,
    verticalalignment="center"
)

# Dashboard title
plt.suptitle("Food Item Performance Dashboard", fontsize=18)
plt.tight_layout()
plt.savefig("food_dashboard.png",dpi=300,bbox_inches="tight")
plt.show()
