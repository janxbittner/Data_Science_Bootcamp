#%% Importing modules
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()

#%% Import data to dataframe
raw_day = pd.read_csv('.\source_data\day.csv',index_col=1)

#%% Create correlation matix
corr_mtx = raw_day.corr()

#%% Filter correlation values
corr_mtx =corr_mtx[corr_mtx > 0.8]
corr_mtx = corr_mtx[corr_mtx != 1]
corr_mtx = corr_mtx.dropna(how='all',axis=1)

#%% Create heat map with correlation matrix
sns.heatmap(corr_mtx)

#%% Create list with high correlated column
high_corr_var=np.where(corr_mtx>0.8)
high_corr_var=[(corr_matrix.index[x],corr_matrix.columns[y]) for x,y in zip(*high_corr_var) if x!=y and x<y]
#%% Print names of high correlated columns
print('High correlated columns:')
for name in high_corr_var: print(name) 