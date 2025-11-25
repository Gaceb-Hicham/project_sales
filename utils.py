import numpy as np
import pandas as pd



def generate_sales(min_val , max_val):
    return np.random.randint(min_val, max_val + 1, size= 12)


dates = pd.date_range(start = '2025-01-01', end = '2025-12-01', freq='MS')

sales_A=generate_sales(50, 100)
sales_B=generate_sales(30, 80)
sales_C=generate_sales(20, 60)
sales_D=generate_sales(10, 50)

df_initial = pd.DataFrame({
    'Date': dates,
    'Product_A': sales_A,
    'Product_B': sales_B,
    'Product_C': sales_C,
    'Product_D': sales_D
})


df_initial.to_csv('data/initial.csv', index=False)

df_final=df_initial.copy()
df_final=df_final.rename(columns={
    'Date':'Month'})

df_final['Month'] = df_final['Month'].dt.strftime('%B %Y')
df_final['Total_Sales'] = df_final[['Product_A', 'Product_B', 'Product_C', 'Product_D']].sum(axis=1)
df_final['Average_Sales'] = df_final[['Product_A', 'Product_B', 'Product_C', 'Product_D']].mean(axis=1).round(2)
df_final['Month_Over_Month_Growth']=df_final['Total_Sales'].pct_change()

def assign_quarter(month_str):
    month = int(month_str.split('-')[1])
    if month <= 3:
        return 'Q1'
    elif month <= 6:
        return 'Q2'
    elif month <= 9:
        return 'Q3'
    else:
        return 'Q4'
    
df_final['Quarter'] = df_final['Month'].apply(lambda x: assign_quarter(pd.to_datetime(x).strftime('%Y-%m')))
# df_final['Quarter'] = df_final['Month'].apply(lambda x: assign_quarter(pd.to_datetime(x).month))

df_final['Max_Sales_Product']=df_final[['Product_A', 'Product_B', 'Product_C', 'Product_D']].idxmax(axis=1)
df_final['Min_Sales_Product']=df_final[['Product_A', 'Product_B', 'Product_C', 'Product_D']].idxmin(axis=1) 

df_final.to_csv('data/final.csv', index=False)
print(df_final)

