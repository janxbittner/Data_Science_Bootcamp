#%% Importing modules
import pandas as pd

#%% Import two dataframes from website
df_1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
df_2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'B': ['B0', 'B1', 'B2']})
#%% Inner join
eg_inner = df_1.join(df_2,how = 'inner', lsuffix= '_left',rsuffix = '_right')

#%% Outer join
eg_outer = df_1.join(df_2,how = 'outer', lsuffix= '_left',rsuffix = '_right')

#%% Left join
eg_left = df_1.join(df_2,how = 'left', lsuffix= '_left',rsuffix = '_right')

#%% Right join
eg_right = df_1.join(df_2,how = 'right', lsuffix= '_left',rsuffix = '_right')