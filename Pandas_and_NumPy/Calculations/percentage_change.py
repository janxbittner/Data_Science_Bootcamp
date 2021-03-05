#%% Importing modues
import pandas as pd
import seaborn as sns
sns.set()
sns.set_style("darkgrid")

#%% Import UBER stock data to data frame
uber_df = pd.read_csv('./source_data/UBER.csv', index_col= 0 )

#%% Remove Adj Close column
del uber_df['Adj Close']

#%% Create new column and calculate in it daily procentage change
uber_df['Daily_change_%'] = uber_df['Close'].pct_change() * 100

#%% Create new column and calculate in it daily procentage change
uber_df['5_Days_change_%'] = uber_df['Close'].pct_change(periods = 5) * 100

#%% Create new column and calculate open to close value
uber_df['Open_to_close_%'] = (uber_df[['Open','Close']].pct_change(axis = 1) * 100)\
    .drop('Open',axis = 1)

#%% Import uber and lyft stocks to data frame
uber_df = pd.read_csv('./source_data/UBER.csv',index_col = 0)
lyft_df = pd.read_csv('./source_data/LYFT.csv',index_col = 0)

#%% Create new df with only prices from Uber stock
prices_df = uber_df[['Open','High','Low','Close']]
    
#%% Create new data frame with only procentage change
pro_change_df = prices_df.pct_change() * 100

#%% Change the columns name in pro_change_df
for col_name in pro_change_df.columns:
    pro_change_df.rename(columns={col_name:col_name + '_pct_change_in_%'}, inplace=True)

#%% Plot line chart of close_pct_change
pro_change_df['Close_pct_change_in_%'].plot(color = 'red')