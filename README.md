# Customer Sales Analysis

A Python-based data analysis project that combines customer and sales datasets, performs data cleaning and transformation, and generates business insights through summary statistics and visualizations.

---

## Project Overview

This project analyzes customer purchasing behavior by:

- Cleaning and validating customer and sales data
- Merging customer and sales datasets
- Calculating transaction amounts
- Identifying the most frequently used payment methods
- Determining which payment methods transfer the most money
- Analyzing spending patterns across age groups
- Generating a customer sales analysis report with key business metrics

---

## Dataset Requirements

### customer_data.csv

Expected columns:

| Column | Description |
|----------|-------------|
| customer_id | Unique customer identifier |
| age | Customer age |
| gender | Customer gender |
| payment_method | Payment method used by customer |

### sales_data.csv

Expected columns:

| Column | Description |
|----------|-------------|
| customer_id | Customer identifier |
| invoice_no | Invoice number |
| quantity | Quantity purchased |
| price | Unit price |
| category | Product category |
| shopping_mall | Shopping mall/store |

---

## Features

### 1. Data Cleaning

The script performs:

- Removal of null values
- Removal of duplicate records

```python
sdata.dropna(inplace=True)
cdata.dropna(inplace=True)

sdata.drop_duplicates(inplace=True)
cdata.drop_duplicates(inplace=True)
```

---

### 2. Data Integration

Customer and sales data are merged using:

```python
master_data = cdata.merge(
    sdata,
    on='customer_id',
    how='inner'
)
```

A new column is created:

```python
amount = quantity × price
```

---

### 3. Most Common Payment Method

Calculates the payment method used in the highest number of unique transactions.

```python
master_data.groupby('payment_method')['invoice_no'].nunique()
```

Visualization:

- Bar Chart
- X-axis: Payment Method
- Y-axis: Number of Transactions

---

### 4. Payment Method Generating Highest Revenue

Calculates total transaction value by payment method.

```python
master_data.groupby('payment_method')['amount'].sum()
```

Visualization:

- Pie Chart
- Percentage contribution of each payment method

---

### 5. Age-wise Expenditure Analysis

Customers are grouped into age brackets:

| Age Group |
|------------|
| 18–23 |
| 23–28 |
| 28–33 |
| 33–38 |
| 38–43 |
| 43–48 |
| 48–53 |
| 53–58 |
| 58–63 |
| 63–69 |

For each group:

```python
total expenditure = sum(amount)
```

Visualization:

- Line Chart
- X-axis: Age Group
- Y-axis: Total Expenditure

---

### 6. Customer Sales Analysis Report

The script prints the following KPIs:

#### Total Revenue

```python
master_data['amount'].sum()
```

#### Total Customers

```python
master_data['customer_id'].nunique()
```

#### Average Order Value (AOV)

Calculated as:

```text
Average of total invoice amounts
```

Formula:

```text
AOV = Mean(Sum of Amount per Invoice)
```

#### Highest Spending Customer

Determined using:

```python
master_data.groupby('customer_id')['amount'].sum()
```

Output:

```text
Customer ID - Total Spend
```

---

## Output Files

### master_data.csv

Generated after merging customer and sales datasets.

Contains:

- Customer information
- Sales information
- Calculated amount field

---

## Visualizations Generated

### Transactions per Payment Method

Bar chart showing transaction count by payment method.

### Amount Transferred per Payment Method

Pie chart showing percentage contribution of revenue by payment method.

### Age-wise Expenditure

Line chart showing spending trends across age groups.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/customer-sales-analysis.git
cd customer-sales-analysis
```

Install required packages:

```bash
pip install pandas matplotlib
```

---

## Running the Project

Place the following files in the project directory:

```text
customer_data.csv
sales_data.csv
```

Run:

```bash
python customer_sales_analysis.py
```

---

## Example Console Output

```text
CUSTOMER SALES ANALYSIS REPORT

Total Revenue : 25,648,430.00
Total Customers : 9,876
Average Order Value : 1,245.37
Top Customer : 12345 - 85,920.00
```

---

## Technologies Used

- Python
- Pandas
- Matplotlib

---

## Future Enhancements

Potential additions:

- Gender-wise spending analysis
- Category-wise revenue analysis
- Monthly and seasonal sales trends
- Customer segmentation
- Interactive dashboards using Plotly or Power BI
- Export reports to Excel or PDF

---

## Author

**Prathamesh**

Customer Sales Analysis Project
