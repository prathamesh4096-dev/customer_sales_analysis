# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:34:18 2026

@author: Prathamesh
"""

#%%
import pandas as pd
import matplotlib.pyplot as plt

cdata = pd.read_csv("customer_data.csv")
sdata = pd.read_csv("sales_data.csv")

#s_sample = sdata.head(10)
#c_sample = cdata.head(10)

#%%
#Data cleaning. 

sdata.dropna(inplace = True)                                                    #Dropping null entries
cdata.dropna(inplace = True)

sdata.drop_duplicates(inplace = True)                                           #Dropping duplicate entries
cdata.drop_duplicates(inplace = True)

#cats = sdata['category'].unique()
#malls = sdata['shopping_mall'].unique()
#gen = cdata['gender'].unique()
#pay = cdata['payment_method'].unique()                                         #Observing values of columns to determine whether further cleaning is needed.

#%%
#Merging the dataframes.

master_data = cdata.merge(sdata, on = 'customer_id', how = 'inner')
#m_sample = master_data.head(10)

master_data['amount'] = master_data['quantity'] * master_data['price']                #Creating an 'amount' column for future use

master_data.to_csv('master_data.csv')

#%%

#Most common payment method
pay_method = master_data.groupby('payment_method')['invoice_no'].nunique()
print(pay_method[pay_method == pay_method.max()])

#Visualizing the number of transactions performed using the different payment methods.

pay_method.plot(kind='bar')

plt.title('Transactions per Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=0)
plt.show()

#%%

#Payment method that transfers the most money
pay_quant_method = (
    master_data['amount']
    .groupby(master_data['payment_method'])
    .sum()
)
print(pay_quant_method[pay_quant_method == pay_quant_method.max()])

#Visualizing the relative amounts of money transferred by different payment methods.

pay_quant_method.plot(kind = 'pie', autopct = '%1.2f%%')

plt.title('Amount transferred per Payment Method')
plt.ylabel('')

plt.show()

#%%

#Visualization of expenditure by age groups
#print(master_data['age'].max())
#print(master_data['age'].min())


# Create amount column
master_data['amount'] = master_data['quantity'] * master_data['price']

# Defining age bins and labels
bins = [18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 69]
labels = [
    '18-23', '23-28', '28-33', '33-38', '38-43',
    '43-48', '48-53', '53-58', '58-63', '63-69'
]

# Creating age groups
master_data['age_group'] = pd.cut(
    master_data['age'],
    bins=bins,
    labels=labels,
    right=True,
    include_lowest=True
)

# Calculating total amount by age group
age_group_amount = (
    master_data.groupby('age_group')['amount']
    .sum()
)

# Plot line graph
plt.figure(figsize=(10, 5))
plt.plot(age_group_amount.index, age_group_amount.values, marker='o')

plt.title('Age-wise Expenditure')
plt.xlabel('Age Group')
plt.ylabel('Total Amount')
plt.grid(True)
plt.xticks(rotation=45)

plt.show()

#%%
#CUSTOMER SALES ANALYSIS REPORT


print('CUSTOMER SALES ANALYSIS REPORT')

#Total customer revenue
total_revenue = master_data['amount'].sum()
print(f"Total Revenue : {total_revenue:,.2f}")

#Total number of customers
cust_count = master_data['customer_id'].nunique()
print(f"Total Customers : {cust_count}")

#Average value of purchase
avg_val = (
    master_data.groupby('invoice_no')['amount']
    .sum()
    .mean()
)
print(f'Average Order Value : {avg_val:,.2f}')

#Highest spending customer.
cust = (
    master_data.groupby('customer_id')['amount']
    .sum()
)
top_cust = cust[cust == cust.max()].reset_index()
tc = top_cust.iloc[0]
print(f'Top Customer : {tc.customer_id} - {tc.amount}')
