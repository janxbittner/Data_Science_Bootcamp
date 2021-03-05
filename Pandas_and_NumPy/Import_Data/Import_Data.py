"""IMPORTING DATA"""

#%% Load modules
import pandas as pd

#%% Import CSV file to data frame
raw_google_data = pd.read_csv('./Data_Source/GOOG.csv',index_col= 0, sep = ',',\
                       skiprows= 100,nrows = 1000)

#%% Importing tsv file
raw_google_data_2 = pd.read_csv('./Data_Source/GOOG.tsv',index_col= 0, sep = '\t',\
                       skiprows= 100,nrows = 1000)
    
#%% Compare two above data frames
print("The same data imported!" if raw_google_data.equals(raw_google_data_2)\
      else "Not the same data!")
    
#%% Import data from excel only SalesOrders sheet
salesOrders_raw_data = pd.read_excel('./Data_Source/SampleData.xlsx',\
                                     sheet_name = 'SalesOrders', index_col = 0)
    
#%% Importing list of Data frame form websites
list_of_df_in_file = pd.read_html('./Data_Source/Data.html')

#%% From list of df import first table
first_table = list_of_df_in_file[0]

#%% Form html file import second table directly to data frame
Second_Table = pd.read_html('./Data_Source/Data.html')[1] 

#%% Import table form website:
car_tax_table = pd.read_html('https://www.gov.uk/vehicle-tax-rate-tables')[0]

# Cleaning the data
car_tax_table.columns = ['CO2 emissions (g/km)',
       'Diesel cars (TC49) that meet the RDE2 standard and petrol cars (TC48) in £',
       'All other diesel cars (TC49) in £', 'Alternative fuel cars (TC59) in £']

# Convert first column to comparable int values
car_tax_table['Diesel cars (TC49) that meet the RDE2 standard and petrol cars (TC48) in £']=\
car_tax_table['Diesel cars (TC49) that meet the RDE2 standard and petrol cars (TC48) in £']\
    .apply(lambda val : int(val.replace('£','').replace(',','')))
    
# Convert other columns to int
car_tax_table['All other diesel cars (TC49) in £']=\
car_tax_table['All other diesel cars (TC49) in £']\
    .apply(lambda val : int(val.replace('£','').replace(',','')))

car_tax_table['Alternative fuel cars (TC59) in £']=\
car_tax_table['Alternative fuel cars (TC59) in £']\
    .apply(lambda val : int(val.replace('£','').replace(',','')))
    
#%% Imporing form SAS

airline_df = pd.read_sas('./Data_Source/airline.sas7bdat', index= 'YEAR')