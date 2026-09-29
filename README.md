# 📊 Sales Customer Analytics

A data analytics project that analyzes sales, customers, products, discounts, regions, and profitability using **Python, Pandas, Matplotlib, MySQL, and SQL**.

The project follows a complete data analytics workflow:

**Data → Cleaning → Analysis → SQL → Visualization → Business Insights**

---

## 🎯 Project Objective

The main objective of this project is to analyze sales data and identify meaningful business insights related to:

- Sales and profit performance
- Customer behavior
- Product performance
- Category and sub-category performance
- Regional sales
- Discount and profitability
- Monthly sales trends

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **MySQL**
- **SQL**
- **Jupyter Notebook**
- **VS Code**

---

## 📂 Project Structure

```text
Sales-Customer-Analytics/
│
├── data/
│   └── sales_data.csv
│
├── notebooks/
│   └── sales_analysis.ipynb
│
├── src/
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── load_data_to_mysql.py
│
├── visualization/
│   ├── monthly_sales.png
│   ├── category_sales.png
│   ├── top_products.png
│   ├── regional_sales.png
│   ├── discount_vs_profit.png
│   └── subcategory_profit_margin.png
│
├── sql/
│   └── sales_analysis.sql
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

The dataset contains **10,194 sales records** and **21 original columns**.

It includes information about:

- Orders
- Customers
- Products
- Categories
- Regions
- Sales
- Quantity
- Discounts
- Profit
- Order and shipping dates

Additional date-based features were created during the analysis.

---

## 🧹 Data Cleaning

The data cleaning process was performed using Pandas.

### Main Steps

- Loaded the CSV dataset
- Converted order and shipping dates to datetime format
- Checked for missing values
- Checked for duplicate records
- Created Year and Month features
- Created Month Name
- Created Year-Month for time-based analysis

### Data Quality

| Metric | Value |
|---|---:|
| Rows | 10,194 |
| Original Columns | 21 |
| Missing Values | 0 |
| Duplicate Rows | 0 |

---

## 📈 Exploratory Data Analysis

The project performs analysis across several business dimensions.

### 1. Overall Business Metrics

The following key metrics were calculated:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Average Order Value

### 2. Category Analysis

Sales, profit, quantity, and profit margin were analyzed across:

- Technology
- Furniture
- Office Supplies

### 3. Regional Analysis

Sales, profit, and quantity were compared across:

- West
- East
- Central
- South

### 4. Product Analysis

The top 10 products were identified based on total sales.

### 5. Customer Analysis

The top 10 customers were identified based on total sales, along with their total profit, quantity, and profit margin.

### 6. Discount Analysis

Sales, profit, and quantity were analyzed across different discount levels.

### 7. Sub-Category Analysis

Sales, profit, quantity, and profit margin were analyzed across product sub-categories.

---

## 🗄️ SQL Analysis

The dataset was imported into **MySQL** for SQL-based business analysis.

SQL concepts used include:

- `SELECT`
- `WHERE`
- `GROUP BY`
- `ORDER BY`
- Aggregate Functions
- `CASE`
- Common Table Expressions (CTEs)
- Window Functions
- `RANK()`

The SQL queries are available in:

```text
sql/sales_analysis.sql
```

---

## 📊 Visualizations

The project generates the following visualizations using Matplotlib:

### Monthly Sales Trend

Shows how sales changed over time.

### Sales by Category

Compares total sales across product categories.

### Top 10 Products by Sales

Highlights the products generating the highest sales.

### Sales by Region

Compares sales performance across different regions.

### Discount vs Total Profit

Shows the relationship between discount levels and total profit in the dataset.

### Profit Margin by Sub-Category

Compares profitability across different product sub-categories.

All generated charts are stored in:

```text
visualization/
```

---

## 💡 Key Business Insights

Based on the analysis:

- Technology generated the highest total sales and profit among the three categories.
- Furniture generated substantial sales but had a considerably lower profit margin.
- The West region recorded the highest total sales and profit.
- Copiers generated the highest total profit among the sub-categories.
- Tables recorded a negative total profit.
- Bookcases and Supplies also recorded negative profit margins.
- Higher discount levels were associated with negative total profit in this dataset.
- Some high-sales customers generated negative profit, showing that sales revenue alone does not indicate customer profitability.
- Some high-sales products also generated low or negative profit.
- The dataset contains **804 unique customers**.
- The dataset contains **5,111 unique orders**.
- The average order value is approximately **455.20**.

> **Note:** The discount analysis shows an association between discount levels and profitability in this dataset; it does not by itself establish that discounts caused the losses.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Sales-Customer-Analytics
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Run data cleaning

```bash
python src/data_cleaning.py
```

### 7. Run the analysis

```bash
python src/analysis.py
```

The analysis script generates the visualizations inside:

```text
visualization/
```

---

## 📌 Project Highlights

This project demonstrates practical experience with:

- Data loading and preprocessing
- Data quality checking
- Pandas data manipulation
- GroupBy and aggregation
- Business metric calculation
- Customer and product analysis
- Profitability analysis
- SQL-based analysis using MySQL
- Data visualization
- Business insight generation

---

## 👩‍💻 Author

**Saniga Sudheer**

B.Tech Computer Science and Engineering

**Aspiring Data Analyst**

**Skills:** Python | SQL | Power BI | Excel | Pandas | Data Visualization