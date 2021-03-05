''' 
TO DO IN CASE STUDY:
    - Import amazon review data,
    - Prepare date to analisis,
    - Analitics
    -
    -
    
    '''
    
#%% Import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%% Read data from csv
r_data = pd.read_csv('./Amaz_review.csv', index_col = 0,)

#%% Take form data only random 5000 rows
r_data = r_data.sample(n = 5000)

#%% Show parameters of imported data
print(r_data.describe())

#%% Print all columns name
print("Columns names:")
for name in r_data.columns: print(name)

#%% Replace dot in column name to underscore
r_data.columns = [name.replace('.','_') for name in r_data.columns ]

#%% Print all columns name
print("Columns names:")
for name in r_data.columns: print(name)

#%% Remove unlesses columns
rew_df = r_data[['name', 'primaryCategories','reviews_rating', 'reviews_text']]

#%% Columns rename
rew_df.columns = ['name','category','rating','reviews'] 

#%% Finnaly data check
print(rew_df.info())
print(rew_df.describe())

#%% Save processed data to csv file
rew_df.to_csv('./proc_amaz_review.csv')

#%% 
'''
DATA ANALITICS
'''

#%% Plot frequency of categories of products
rew_df.category.value_counts().plot(kind = 'pie', title = 'Category frequency')

#%% Plot frequency of products mark
rew_df.rating.value_counts().sort_index().plot(kind = 'bar', legend = True,\
                                               title = 'Rating frequency')
    
#%% Plot top 3 most rating products by count
top_3 = pd.pivot_table(rew_df, index = 'name', aggfunc= {'rating':'count' })
top_3 = top_3.nlargest(3,'rating')
top_3.columns = ['count']
top_3.plot(kind = 'bar')

#%% Plot top 3 most rating products by mark
top_3_mark = rew_df.groupby('name').mean()
top_3_mark.columns = ['avg_rating']
top_3_mark = top_3_mark.nlargest(3,columns = 'avg_rating')
top_3_mark.plot(kind = 'bar')

#%% Plot bottom 3 most rating products by mark
bot_3_mark = rew_df.groupby('name').mean()
bot_3_mark.columns = ['avg_rating']
bot_3_mark = bot_3_mark.nsmallest(3,columns = 'avg_rating')
bot_3_mark.plot(kind = 'bar')
