import pandas as pd
import mysql.connector

# 1. Read the CSV file
df = pd.read_csv(
    "data/sales_data.csv",
    encoding="latin1"
)

# Convert date columns from text to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("CSV loaded successfully")
print("Rows:", len(df))


# 2. Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="San@2005",
    database="sales_customer_analytics"
)

cursor = connection.cursor()

print("Connected to MySQL successfully")


# 3. Clear existing data from the table
cursor.execute("TRUNCATE TABLE sales")


# 4. SQL query for inserting data
insert_query = """
INSERT INTO sales (
    row_id,
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id,
    customer_name,
    segment,
    country_region,
    city,
    state_province,
    postal_code,
    region,
    product_id,
    category,
    sub_category,
    product_name,
    sales,
    quantity,
    discount,
    profit
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s
)
"""


# 5. Insert each row
for _, row in df.iterrows():

    values = (
        row["Row ID"],
        row["Order ID"],
        row["Order Date"].date(),
        row["Ship Date"].date(),
        row["Ship Mode"],
        row["Customer ID"],
        row["Customer Name"],
        row["Segment"],
        row["Country/Region"],
        row["City"],
        row["State/Province"],
        str(row["Postal Code"]),
        row["Region"],
        row["Product ID"],
        row["Category"],
        row["Sub-Category"],
        row["Product Name"],
        row["Sales"],
        row["Quantity"],
        row["Discount"],
        row["Profit"]
    )

    cursor.execute(insert_query, values)


# 6. Save changes
connection.commit()

print("Data imported successfully!")


# 7. Check number of rows in MySQL
cursor.execute("SELECT COUNT(*) FROM sales")

count = cursor.fetchone()[0]

print("Rows in MySQL:", count)


# 8. Close connection
cursor.close()
connection.close()

print("MySQL connection closed.")