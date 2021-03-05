"""Conecting Data method"""

#%% Importing modules
import pandas as pd
import numpy as np

#%% Create random three dataframes and one series
df1 = pd.DataFrame(np.random.rand(10,5))
df2 = pd.DataFrame(np.random.rand(10,5))
df3 = pd.DataFrame(np.random.rand(10,5))
rand_series = pd.Series(np.random.rand(10),name = 'rand val')

#%% Connect three dataframe using contact method
concat_df = pd.concat([df1,df2,df3])

#%% Reset index in concat_df
concat_df = concat_df.reset_index()

#%% Contact the data and set continous int index in one line
df_one_line = pd.concat([df1,df2,df3],ignore_index= True)

#%% Create two dataframe with different column name but same indexes
df11 = pd.DataFrame(np.random.rand(10,5), columns= list('abcde'))
df22 = pd.DataFrame(np.random.rand(10,5), columns= list('fghij'))

#%% Connect two dataframe with the same indexes
df_index_conect = pd.concat([df11,df22],axis = 1)

#%% Romove form df1 every second index
df1 = df1[::2]

#%% Connect df1 and df2 but only existing indexes in bouth dataframe
outer_connect = pd.concat([df1,df2],join = 'inner', axis = 1)

#%% Connect dataframe with series
df_and_series = pd.concat([df3,rand_series],axis = 1)

#%%
'''APPEND METHOD'''

#%% Connect df1 and df2 using append method
appended_df = df1.append(df2,ignore_index = True)

#%% 
'''MERGE METHOD'''