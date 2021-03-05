#%% Importing modues
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()

#%% Create data frame with random 1000 elements and date indexes
rand_df = pd.DataFrame(np.random.randn(1000,5), index = pd.\
                        date_range(start = '29-08-2020', periods = 1000),\
 
                            columns = list('ABCDE'))
#%% Calculate cumulate sum of df
rand_df = rand_df.cumsum()

#%% Apply each values to abs
rand_df = rand_df.apply(abs)
    
#%% Plot the close data
rand_df.iloc[-1].plot(kind = 'bar', title = 'Last values of each column.')

#%% Load data to data frame
products_costs = pd.DataFrame(np.random.randint(10, size=(4, 4)))

#%% Plot multiple vertical bar char
products_costs.plot(kind = 'bar',cmap = 'Oranges',alpha = 0.8, title ='Products costs')

#%% Plot multiple horizontal bar char
products_costs.plot.barh(cmap = 'Oranges',alpha = 0.8, title ='Products costs')

#%% Plot stacked multiple vertical bar char
products_costs.plot.bar(stacked = True, cmap = 'Oranges',alpha = 0.8, title ='Products costs')

#%% Plot stacked multiple horizontal bar char
products_costs.plot.barh(stacked = True, cmap = 'Oranges',alpha = 0.8, title ='Products costs')