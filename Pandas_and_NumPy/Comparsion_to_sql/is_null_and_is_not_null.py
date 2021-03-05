#%% Importing modules
import pandas as pd

#%% Import data
r_data = pd.read_csv('./source_data/retail.csv')

#%% Select all rows and columns where  InvoiceNo is null
s_null = r_data[r_data['InvoiceNo'].isnull()]

#%% Select all rows and columns where  InvoiceNo is not null
s_not_null = r_data[r_data['InvoiceNo'].notnull()]