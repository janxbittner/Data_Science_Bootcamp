#%% Importing modules
import pandas as pd
import seaborn as sns
sns.set()

#%% Import data
r_data = sns.load_dataset('tips')

#%% Create pivot table
pivot_st = pd.pivot_table(r_data, values = ['tip','total_bill'], index= 'sex', columns =\
                          ['day','smoker'], aggfunc = 'min')
    
#%% Round values in pivot_st
pivot_st = pivot_st.round(2)

#%% Plot tip by sex and day
pd.pivot_table(r_data, values = 'tip', index= 'sex', columns ='day',
               aggfunc = 'mean').plot(kind = 'bar', cmap = 'viridis', alpha = 0.5)

#%% Plot total bill by sex and day
pd.pivot_table(r_data, values = 'total_bill', index= 'sex', columns ='day',
               aggfunc = 'mean').plot(kind = 'bar', cmap = 'viridis', alpha = 0.5)

#%% Plot person quantity to tip values
pd.pivot_table(r_data, values = 'total_bill', index= 'day', columns ='size',
               aggfunc = 'mean').plot(kind = 'bar', cmap = 'viridis', alpha = 0.5)

#%% Plot day time to tip values
pd.pivot_table(r_data, values = 'total_bill', index= 'time', columns ='size',
               aggfunc = 'mean').plot(kind = 'bar', cmap = 'viridis', alpha = 0.5)

#%% Calculate correlation values by tip and total bill
corr = r_data['tip'].corr(r_data['total_bill'])