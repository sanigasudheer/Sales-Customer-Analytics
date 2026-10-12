
# 📊 Sales Customer Analytics

An end-to-end data analytics project analyzing sales performance, customer behavior, product trends, regional performance, discounts, and profitability using **Python, Pandas, MySQL, SQL, and Power BI**.

The project follows a complete data analytics workflow:

**Data → Cleaning → EDA → SQL Analysis → Visualization → Power BI Dashboard → Business Insights**

## 🎯 Project Objective

The objective is to analyze sales data and identify meaningful business insights related to:

- Sales and profit performance
- Customer behavior
- Product performance
- Category and sub-category performance
- Regional sales and profitability
- Discounts and profit margins
- Monthly sales trends

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- MySQL
- SQL
- Microsoft Power BI
- DAX
- Jupyter Notebook
- VS Code

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
├── Sales_Customer_Analytics_Dashboard.pbix
├── README.md
└── requirements.txt
```

## 📊 Dataset

The dataset contains **10,194 sales records** and **21 original columns**.

It includes information about:

- Orders and customers
- Products and categories
- Regions
- Sales and quantity
- Discounts and profit
- Order and shipping dates

Additional date-based features were created during the analysis.

## 🧹 Data Cleaning

Data cleaning was performed using Pandas.

### Main Steps

- Loaded the CSV dataset
- Converted order and shipping dates to datetime format
- Checked for missing values
- Checked for duplicate records
- Created Year and Month features
- Created Month Name
- Created Year-Month for time-based analysis

### Data Quality Summary

| Metric | Value |
|---|---:|
| Rows | 10,194 |
| Original Columns | 21 |
| Missing Values | 0 |
| Duplicate Rows | 0 |

## 📈 Exploratory Data Analysis (EDA)

### 1. Overall Business Metrics

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Average Order Value

### 2. Category Analysis

Analyzed sales, profit, quantity, and profit margin across:

- Technology
- Furniture
- Office Supplies

### 3. Regional Analysis

Compared sales, profit, and quantity across:

- West
- East
- Central
- South

### 4. Product Analysis

Identified the top 10 products based on total sales.

### 5. Customer Analysis

Identified the top 10 customers by sales and analyzed their profit, quantity, and profit margin.

### 6. Discount Analysis

Analyzed sales, profit, and quantity across different discount levels.

### 7. Sub-Category Analysis

Compared sales, profit, quantity, and profit margin across product sub-categories.

## 🗄️ SQL Analysis

The dataset was imported into MySQL for SQL-based business analysis.

### SQL Concepts Used

- SELECT and WHERE
- GROUP BY and ORDER BY
- Aggregate Functions
- CASE Statements
- Common Table Expressions (CTEs)
- Window Functions
- RANK()

**SQL file:** `sql/sales_analysis.sql`

## 📊 Python Visualizations

Matplotlib was used to create the following visualizations:

| Visualization | Purpose |
|---|---|
| Monthly Sales Trend | Analyzes sales over time |
| Sales by Category | Compares category sales |
| Top 10 Products by Sales | Identifies top-performing products |
| Sales by Region | Compares regional sales |
| Discount vs Total Profit | Examines discount levels and profitability |
| Profit Margin by Sub-Category | Compares sub-category profitability |

All generated charts are stored in the `visualization/` directory.

## 📉 Power BI Dashboard

An interactive **Sales Overview Dashboard** was developed using Microsoft Power BI to present business performance through KPIs and visualizations.

### Dashboard Features

- **Total Sales:** Overall sales performance
- **Total Profit:** Overall profitability
- **Total Orders:** Distinct order count
- **Profit Margin:** Profit as a percentage of sales
- **Monthly Sales Trend:** Tracks sales over time
- **Sales by Category:** Compares category performance
- **Profit by Category:** Analyzes category profitability
- **Sales by Region:** Compares regional sales
- **Profit by Region:** Compares regional profitability
- **Sales vs Profit by Region:** Compares sales and profit
- **Region Slicer:** Filters dashboard visuals interactively

### Dashboard Preview

<!-- Upload your screenshot to a screenshots folder and uncomment this line. -->

<!-- ![Sales Overview Dashboard](screenshots/sales_dashboard.png) -->

### Power BI Report

Download the `.pbix` file from the repository and open it using Microsoft Power BI Desktop.

**Report file:** `Sales_Customer_Analytics_Dashboard.pbix`

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
- Some high-sales products generated low or negative profit.
- The dataset contains **804 unique customers**.
- The dataset contains **5,111 unique orders**.
- The average order value is approximately **455.20**.

**Note:** The discount analysis shows an association between discount levels and profitability. It does not, by itself, establish that discounts caused the losses.

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/sanigasudheer/Sales-Customer-Analytics.git
```

### 2. Navigate to the Project Directory

```bash
cd Sales-Customer-Analytics
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Data Cleaning

```bash
python src/data_cleaning.py
```

### 7. Run Analysis

```bash
python src/analysis.py
```

The analysis script generates visualizations in the `visualization/` directory.

### 8. Open the Power BI Dashboard

1. Download the `.pbix` report from the repository.
2. Open it in Microsoft Power BI Desktop.
3. If prompted, update the data source path to match your local CSV file.
4. Refresh the data if required.

*Note: Running the MySQL analysis may require a separately configured MySQL server and database.*

## 📌 Project Highlights

This project demonstrates practical experience with:

- Data cleaning and preprocessing
- Exploratory Data Analysis
- Pandas data manipulation and aggregation
- Customer and product analysis
- Sales and profitability analysis
- SQL querying using MySQL
- Data visualization using Matplotlib
- Power BI dashboard development
- DAX measures and KPI reporting
- Interactive data filtering
- Business insight generation

## 👩‍💻 Author

**Saniga Sudheer**

B.Tech Computer Science and Engineering

Aspiring Data Analyst

**Skills:** Python | SQL | Power BI | Excel | Pandas | Data Visualization
