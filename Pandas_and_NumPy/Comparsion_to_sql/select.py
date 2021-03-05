#%% Importing modules
import pandas as pd

#%% Import data
URL= ('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/'
      'Online%20Retail.xlsx')
r_data = pd.read_excel(URL)

#%% Save the raw data
retail_df = r_data.copy()
r_data.to_csv('./source_data/retail.csv')
 
#%% Check if in dataset is any empty values
retail_df.info()

#%% Create list of columns name
col_names = [col_name for col_name in retail_df.columns]

#%% Show first 10 rows
print(retail_df.head(n = 10))

#%% Show last 10 rows
print(retail_df.tail(n = 10))

#%% Drop rows where customer ID don't exsist
retail_df = retail_df[retail_df['CustomerID'].notnull()]

#%% Convert values in column CustomerID
retail_df['CustomerID'] = [str(int(val)) for val in retail_df['CustomerID']]

#%% Select row with quantity higher then zero
retail_df = retail_df[retail_df['Quantity'] > 0]

#%% Select all rows from retail_df
s_all = retail_df # Select * from retail_df

#%% Select some columns from dataframe
s_columns = retail_df[['Country','Quantity']] # Select Country, Quantity from retail_df

#%% First 10 rows and columns Country and Quantity from DF
s_top_ten = retail_df[['Country','Quantity']][:10]

#%% Select all columns and rows where CustomerID = 17850
s_id = retail_df[retail_df['CustomerID'] == '17850']

#%%
""" SELECT WITH AND/OR"""

#%% Select all columns and rows where CustomerID = 17850 and UnitPrice > 5
s_id_and_unit = retail_df[(retail_df['CustomerID'] == '17850') & (retail_df['UnitPrice'] > 5)]

#%% Select all columns and rows where CustomerID = 17850 and Country == France
s_id_or_country = retail_df[(retail_df['CustomerID'] == '17850') |\
                          (retail_df['Country'] == 'France')]

s_id_or_country = retail_df.query("""CustomerID == '17850' or Country == 'France'""")







