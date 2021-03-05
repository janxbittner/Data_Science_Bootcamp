#%% Importing modules
import pandas as pd
import numpy as np

#%% Import data
r_data = pd.read_csv('./source_data/retail.csv')

#%% Count ordes by customer id
g_cust = r_data.groupby('CustomerID').size()

#%% Count ordes by country
g_cuntry = r_data.groupby('Country').size() 

#%% Calculate reveniue of order
r_data['Revenue'] = r_data['Quantity'] * r_data['UnitPrice']

#%% Grup by customer id and calculate avg reveniue
g_rev = r_data.groupby('CustomerID').agg({'Revenue':np.mean,'CustomerID':np.size})

#%% Create column with ondy invoice day
r_data['Inv_day'] = r_data['InvoiceDate'].apply(lambda x: str(x).split(' ')\
                                                 [0].split('-')[2])
r_data['Inv_day'] = r_data['Inv_day'].apply(lambda x : int(x[1]) if x.startswith('0') else int(x))

#%% Sum revenue by day on invoice
g_sum = r_data.groupby('Inv_day').agg({'Revenue':'sum'})

#%% Sort index in g_sum
g_sum = g_sum.sort_index()

#%% Plot reveniue values by number of day
g_sum.plot(kind = 'bar', color ='black', alpha = 0.5, title = 'Revenue by day')

#%% Create column with date format
r_data['Date'] = pd.to_datetime(r_data['InvoiceDate'])

#%% Create column with hour
r_data['hour'] = r_data['Date'].dt.hour

#%% Create column with hour
one_day = r_data[r_data['Inv_day'] == 7]

#%% Show revenue by hour on the 7 th day of monty
g_hour = one_day.groupby('hour').agg({'Revenue':'sum'})

#%% Plot sum of reveniue on the 7 th day of monty depend of hour
g_hour.plot(kind = 'bar', color ='black', alpha = 0.5, title = ('Revenue by'
                                                                ' hour in 7th'
                                                                ' of the month'))
