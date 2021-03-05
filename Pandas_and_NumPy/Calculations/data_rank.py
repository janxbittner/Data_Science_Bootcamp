#%% Importing modues
import pandas as pd
import seaborn as sns
sns.set()
sns.set_style("darkgrid")

#%% Import UBER stock data to data frame
uber_df = pd.read_csv('./source_data/UBER.csv', index_col= 0 )

#%% Create series with Uber stock volume
uber_vol = uber_df[['Volume']]

#%% Create new column and calculate in it volume rank
uber_vol['Volume_rank'] = uber_vol['Volume'].rank()

#%% Sort data frame by Volume rank
uber_vol = uber_vol.sort_values(by = 'Volume_rank', ascending = False)

#%% Create new df with 10 higest volume values
top_10 = uber_vol.nlargest(n= 10, columns = 'Volume')

#%% Create bar char with top 10 volumes
top_10['Volume'].plot.bar(title = '10 highest Uber Volume')

#%% Create new df with only prices from Uber stock
prices_df = uber_df[['Open','High','Low','Close']]
    
#%% Create new data frame with ranked all values by columns
uber_rank_by_col = uber_df.rank(method = 'first')

#%% Create new data frame with ranked all values by rows
uber_rank_by_row = uber_df.rank(method = 'first',axis = 1)