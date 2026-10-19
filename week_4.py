import numpy as np
import pandas as pd
data = pd.read_csv('Online_Retail.csv')

print(data.head())
print(data.info())
print(data.columns)
print(data.Country.unique())
data['Description'] = data['Description'].str.strip()
data.dropna(axis = 0, subset =['InvoiceNo'], inplace = True)
data['InvoiceNo'] = data['InvoiceNo'].astype('str')
data = data[~data['InvoiceNo'].str.contains('C')]