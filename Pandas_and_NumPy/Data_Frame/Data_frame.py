# -*- coding: utf-8 -*-

#%% Import modules

import pandas as pd
import numpy as np

#%%
"""
CREATE OBJECTS DATA FRAME
"""

# Create a df form list
n_list = [1,2,5,9]
df_f_list = pd.DataFrame(n_list,columns= ["Values"], index = range(1,len(n_list)+1))

# Create a df from nested list
nested_list = [[2,4,8,10],[3,9,12,15]]
df_f_nested_l = pd.DataFrame(nested_list)

# Create a df form dictionary

n_dict = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}
df_f_dict = pd.DataFrame(n_dict)

# Create a df form list of dictionary

scnd_dict = {'a':[10,20,30],'b':[40,50,60],'c':[70,80,90]}

df_f_l_of_d = pd.DataFrame([n_dict,scnd_dict])

#  Exercise create a df with fruit in storage
storage_1 = {'apples':3,'banana':4,'cherries':2}
storage_2 = {'apples':2,'banana':6,'Dragon Fruit':3}
storage_3 = {'apples':10,'banana':4,'cherries':2,'Dragon Fruit':3}


storage_df = pd.DataFrame([storage_1,storage_2,storage_3],index= range(1,4) )

# Create a df from dict, then return column and index names

DAX_list = ['Adidas','Allianz','BASF','Bayer']
NASDAQ_list = ['Amazon.com',' Inc.Apollo Group', 'Inc.Apple Inc.']

Stocks_df = pd.DataFrame(data = [DAX_list,NASDAQ_list], index= ['DAX','Nasdaq'])

# Diffrent approach


DAX_series = pd.Series(DAX_list, name = 'DAX')
NASDAQ_series = pd.Series(NASDAQ_list, name = 'Nasdaq')



Stocks_df_d_approach = pd.DataFrame(data = [DAX_series,NASDAQ_series])

#%%
'''
COLUMNS SELECTING
'''
# importing data
stocks = pd.read_csv('./Data/UBER.csv', index_col = 0)

# From a df select only Open and close Values
Open_and_close = stocks.iloc[:,[0,3]]

# Other approach
Open_a_close = stocks[['Open','Close']]

# Assign Volume to series object
Volume = stocks.Volume

#Other approach
Volume_2 = stocks['Volume']

#Other approach
Volume_3 = stocks.iloc[:,-1]

#%%
'''
DATA CUTTING
'''

# importing data
stocks = pd.read_csv('./Data/UBER.csv', index_col = 0)

# Create a df with only data from 2020
stocks2020 = stocks.loc['2020-01-02':]

# Create a df with only data from 2020 and Volume and Close column
stocks2020_two = stocks.loc['2020-01-02':,['Volume','Close']]

# Create a seriers with first 100 rows in High column
Hight_100_First = stocks.iloc[:100,1]


# Create a df with last 100 rows in High and Adj Close columns
Last_100 = stocks.iloc[:-100,[1,-2]]

#%%
'''
CALCULATING NEW COLUMNS
'''

# importing data
stocks = pd.read_csv('./Data/UBER.csv', index_col = 0)

# Create new column called'Average' and calculate average of High and Low prices
stocks['Average'] = (stocks['High'] + stocks['Low']) / 2

# Create new column called'Daily change in percentage' and calculate daily prices change
stocks['Daily change [%]'] = (stocks['Close'] / stocks['Close'].shift(1) - 1) * 100

# Plot Close value
stocks['Close'].plot(figsize = (10,10),title = 'UBER Close Values',grid = True)

# Create column growth and assing Yes if Daily change > 0, No if below
stocks['Growth'] = stocks['Daily change [%]'].apply(lambda val: "Yes" if\
                                                    val > 0 else 'No' )

# Print propability of growth in given data set
print('There is',(((stocks['Growth'] == 'Yes').sum()/stocks['Growth']\
                   .count())*100).round(2),"% chances that UBER value will growth.")
    

#%%
'''
LOGICS MASK

'''

# importing data
stocks = pd.read_csv('./Data/UBER.csv', index_col = 0)

# Create a df only with close value > 30 using Query function
High_Close = stocks.query('Close > 30')

# Remove from High_Close indexes in 2019
High_Close_2020 = High_Close['2020-01-01':]

