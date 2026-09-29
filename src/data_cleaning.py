import pandas as pd


# ============================================
# 1. LOAD DATA
# ============================================

df = pd.read_csv(
    "data/sales_data.csv",
    encoding="latin1"
)

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ============================================
# 2. CONVERT DATE COLUMNS
# ============================================

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


# ============================================
# 3. CHECK MISSING VALUES
# ============================================

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================
# 4. CHECK DUPLICATES
# ============================================

print("\nDuplicate Rows:", df.duplicated().sum())


# ============================================
# 5. CREATE DATE FEATURES
# ============================================

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()
df["Year-Month"] = df["Order Date"].dt.to_period("M")


# ============================================
# 6. DISPLAY FINAL DATA
# ============================================

print("\nData Cleaning Completed!")
print(df.head())