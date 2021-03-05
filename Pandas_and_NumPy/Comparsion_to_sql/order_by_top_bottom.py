#%% Importing modules
import pandas as pd

#%% Import data
r_data = pd.read_csv('./source_data/retail.csv', parse_dates= ['InvoiceDate'])


#%% Show 5 rows ordered by highest values in Quantity column
s_top_5 = r_data.nlargest(n = 5, columns = 'Quantity')

#%% Show 10 rows ordered by lowest values in Quantity column
s_low_10 = r_data.nsmallest(n = 5, columns = 'Quantity')