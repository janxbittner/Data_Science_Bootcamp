"""Conecting Data method"""

#%% Importing modules
import pandas as pd
import matplotlib.pyplot as plt

#%% Import stock data from Uber and lyft company
raw_ub = pd.read_csv('./Data_source/UBER.csv', index_col=0)
raw_lt = pd.read_csv('./Data_source/LYFT.csv', index_col=0)

#%% Create copy of above dfs
uber = raw_ub.copy()
lyft = raw_lt.copy()

#%% Create and calculate on dfs columns named daily change
uber['Daily_change'] = uber['Close']/uber['Close'].shift(1) - 1
lyft['Daily_change'] = lyft['Close']/lyft['Close'].shift(1) - 1

#%%
'''MERGE METHOD'''

#%% Connect df1 and df2 using append method
# Outer indexes include time when uber wasn't on stocks
outer_df = pd.merge(uber,lyft,how = 'outer',left_index=True, right_index= True\
                     ,suffixes = ('_UBER','_LYFT'))
    
# Inner is a df with indexes started with uber on stocks
inner_df = pd.merge(uber,lyft,how = 'inner',left_index=True, right_index= True\
                     ,suffixes = ('_UBER','_LYFT'))
    
#%% Create correlation matrix
Corr_matrix = inner_df.corr(method= 'pearson', min_periods= 10)

#%% Plot close values of Uber and Lyft
plt.plot(inner_df.index, inner_df.Close_UBER, label = "Uber close val")
plt.plot(inner_df.index, inner_df.Close_LYFT, label = "Lyft close val")
plt.xlabel('Time')
plt.ylabel('Close val in $')
plt.title('Comparsion of Uber and Lyft close values.')
plt.legend()
plt.show()

#%%
""" MERGE BY KEY """

#%% Create two dictonaries
shop_1 = {'data':['29-08-2020','01-09-2020','03-09-2020'],\
          'product_id':['0012','2560','1250'],'price':['10.99','8.29','5.99']}
    
shop_2 = {'data':['29-08-2020','01-09-2020','02-09-2020'],\
          'valid':['True','False','False'],'Tax':['0.34','2.21','1.24']}

#%% Create two dataframe from dictonaries
shop_1_df = pd.DataFrame(shop_1)
shop_2_df = pd.DataFrame(shop_2)

#%% Connect dataframes by merge inner
df_inner = pd.merge(shop_1_df, shop_2_df,how = 'inner', on = ['data'])

#%% Connect dataframes by merge outer
df_outer = pd.merge(shop_1_df, shop_2_df,how = 'outer', on = ['data'])

#%% Connect dataframes by merge outer
df_left = pd.merge(shop_1_df, shop_2_df,how = 'left', on = ['data'])

#%% Connect dataframes by merge outer
df_right = pd.merge(shop_1_df, shop_2_df,how = 'right', on = ['data'])

#%%
"""ANOTHER ONE EXAMPLE OF MERGING BY ORDER ID KEY"""

#%% Import two dataframes from website
df_1 = pd.read_html('https://www.w3schools.com/sql/sql_join.asp#:~:text=A%20JOIN%20clause%20is%20used,a%20related%20column%20between%20them.&text=Notice%20that%20the%20%22CustomerID%22%20column,is%20the%20%22CustomerID%22%20column.')[0]
df_2 = pd.read_html('https://www.w3schools.com/sql/sql_join.asp#:~:text=A%20JOIN%20clause%20is%20used,a%20related%20column%20between%20them.&text=Notice%20that%20the%20%22CustomerID%22%20column,is%20the%20%22CustomerID%22%20column.')[2]

#%% Normalize the date format
df_2.OrderDate = df_2.OrderDate.apply(lambda date: date.split('/')[-1]\
                                      + "-" + date.split('/')[0] + '-' \
                                          + date.split('/')[1])
df_2.OrderDate = df_2.OrderDate.apply(lambda date: date.split('-')[0] + '-' \
                                      + '0' + date.split('-')[1] + '-' \
                                          + date.split('-')[2] if \
                                              len(date.split('-')[1]) == 1 \
                                                  else date)

#%% Inner join
eg_inner = pd.merge(df_1,df_2,how = 'inner', on = ['OrderID','OrderDate'])

#%% Outer join
eg_outer = pd.merge(df_1,df_2,how = 'outer', on = ['OrderID','OrderDate'])

#%% Left join
eg_left = pd.merge(df_1,df_2,how = 'left', on = ['OrderID','OrderDate'])

#%% Right join
eg_right = pd.merge(df_1,df_2,how = 'right', on = ['OrderID','OrderDate'])