#%% Importing modues
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()
sns.set_style("darkgrid")

#%% Create series with random 1000 elements and date indexes
rand_series = pd.Series(np.random.randn(1000), index = pd.\
                        date_range(start = '29-08-2020', periods = 1000))

#%% Calculate cumulate sum of series
rand_series = rand_series.cumsum()

#%% Create plot on time series
rand_series.plot()

#%% Create data frame with random 1000 elements and date indexes
rand_df = pd.DataFrame(np.random.randn(1000,5), index = pd.\
                        date_range(start = '29-08-2020', periods = 1000),\
 
                            columns = list('ABCDE'))
#%% Calculate cumulate sum of df
rand_df = rand_df.cumsum()

#%% Create plot on time series
rand_df.plot()

#%% Import uber and lyft stocks to data frame
uber_df = pd.read_csv('./source_data/UBER.csv',index_col = 0)
lyft_df = pd.read_csv('./source_data/LYFT.csv',index_col = 0)

#%% Connect uber and lyft df
connected_df = pd.merge(uber_df['Close'], lyft_df['Close'], how = 'outer',\
                        suffixes= ['_UBER','_LYFT'], left_index= True,\
                            right_index = True)
    
#%% Plot the close data
connected_df.plot()
