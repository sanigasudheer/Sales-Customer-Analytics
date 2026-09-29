import pandas as pd
import matplotlib.pyplot as plt

# Display all columns when printing DataFrames
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

# ============================================
# 1. LOAD CLEANED DATA
# ============================================

df = pd.read_csv(
    "data/sales_data.csv",
    encoding="latin1"
)

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Create date features
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()
df["Year-Month"] = df["Order Date"].dt.to_period("M")


# ============================================
# 2. OVERALL BUSINESS METRICS
# ============================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

average_order_value = total_sales / total_orders


print("============================================")
print("OVERALL BUSINESS METRICS")
print("============================================")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Order Value:", round(average_order_value, 2))

# ============================================
# 3. CATEGORY ANALYSIS
# ============================================

category_analysis = (
    df.groupby("Category", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
)

category_analysis["Profit_Margin"] = (
    category_analysis["Total_Profit"]
    / category_analysis["Total_Sales"]
) * 100

category_analysis = category_analysis.sort_values(
    "Total_Sales",
    ascending=False
)

print("\n============================================")
print("CATEGORY ANALYSIS")
print("============================================")

print(category_analysis)

# ============================================
# 4. REGIONAL ANALYSIS
# ============================================

regional_analysis = (
    df.groupby("Region", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
)

regional_analysis = regional_analysis.sort_values(
    "Total_Sales",
    ascending=False
)

print("\n============================================")
print("REGIONAL ANALYSIS")
print("============================================")

print(regional_analysis)

# ============================================
# 5. TOP 10 PRODUCTS
# ============================================

top_products = (
    df.groupby("Product Name", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
    .head(10)
)

print("\n============================================")
print("TOP 10 PRODUCTS BY SALES")
print("============================================")

print(top_products)

# ============================================
# 6. TOP 10 CUSTOMERS
# ============================================

customer_analysis = (
    df.groupby(
        ["Customer ID", "Customer Name"],
        as_index=False
    )
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
    .head(10)
)

customer_analysis["Profit_Margin"] = (
    customer_analysis["Total_Profit"]
    / customer_analysis["Total_Sales"]
) * 100

print("\n============================================")
print("TOP 10 CUSTOMERS BY SALES")
print("============================================")

print(customer_analysis.to_string(index=False))

# ============================================
# 7. DISCOUNT ANALYSIS
# ============================================

discount_analysis = (
    df.groupby("Discount", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .sort_values("Discount")
)

print("\n============================================")
print("DISCOUNT ANALYSIS")
print("============================================")

print(discount_analysis.to_string(index=False))

# ============================================
# 8. SUB-CATEGORY ANALYSIS
# ============================================

subcategory_analysis = (
    df.groupby("Sub-Category", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
)

subcategory_analysis["Profit_Margin"] = (
    subcategory_analysis["Total_Profit"]
    / subcategory_analysis["Total_Sales"]
) * 100

subcategory_analysis = subcategory_analysis.sort_values(
    "Total_Sales",
    ascending=False
)

print("\n============================================")
print("SUB-CATEGORY ANALYSIS")
print("============================================")

print(subcategory_analysis.to_string(index=False))


# ============================================
# VISUALIZATIONS
# ============================================

# ============================================
# 9. MONTHLY SALES TREND
# ============================================

monthly_sales = (
    df.groupby("Year-Month", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
)

# Convert Year-Month to string for plotting
monthly_sales["Year-Month"] = monthly_sales["Year-Month"].astype(str)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales["Year-Month"],
    monthly_sales["Total_Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig("visualization/monthly_sales.png")

plt.show()

# ============================================
# 10. CATEGORY SALES
# ============================================

plt.figure(figsize=(8, 5))

plt.bar(
    category_analysis["Category"],
    category_analysis["Total_Sales"]
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()

# Save chart
plt.savefig("visualization/category_sales.png")

plt.show()

# ============================================
# 11. TOP 10 PRODUCTS BY SALES
# ============================================

# Sort products for better visualization
top_products_chart = top_products.sort_values(
    "Total_Sales",
    ascending=True
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_products_chart["Product Name"],
    top_products_chart["Total_Sales"]
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")

plt.tight_layout()

# Save chart
plt.savefig("visualization/top_products.png")

plt.show()

# ============================================
# 12. REGIONAL SALES
# ============================================

plt.figure(figsize=(8, 5))

plt.bar(
    regional_analysis["Region"],
    regional_analysis["Total_Sales"]
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()

# Save chart
plt.savefig("visualization/regional_sales.png")

plt.show()

# ============================================
# 13. DISCOUNT VS PROFIT
# ============================================

plt.figure(figsize=(9, 5))

plt.plot(
    discount_analysis["Discount"],
    discount_analysis["Total_Profit"],
    marker="o"
)

plt.title("Discount vs Total Profit")
plt.xlabel("Discount")
plt.ylabel("Total Profit")

plt.axhline(
    y=0,
    linestyle="--"
)

plt.tight_layout()

# Save chart
plt.savefig("visualization/discount_vs_profit.png")

plt.show()

# ============================================
# 14. SUB-CATEGORY PROFIT MARGIN
# ============================================

subcategory_chart = subcategory_analysis.sort_values(
    "Profit_Margin",
    ascending=True
)

plt.figure(figsize=(10, 7))

plt.barh(
    subcategory_chart["Sub-Category"],
    subcategory_chart["Profit_Margin"]
)

plt.title("Profit Margin by Sub-Category")
plt.xlabel("Profit Margin (%)")
plt.ylabel("Sub-Category")

plt.axvline(
    x=0,
    linestyle="--"
)

plt.tight_layout()

# Save chart
plt.savefig("visualization/subcategory_profit_margin.png")

plt.show()