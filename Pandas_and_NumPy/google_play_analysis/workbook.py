''' Google Play store analysis'''

#%% Importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%% Data importing
r_df = pd.read_csv('./googleplaystore.csv')

#%% Check if there are any nan values in data
print(r_df.info())

#%% Create list of columns name
col_names = [name for name in r_df.columns]

#%% Remove spaces in columns name to underscore
r_df.columns = [name.replace(' ','_') for name in r_df.columns]

#%% Create again column name list
col_names = [name for name in r_df.columns]

#%% Remove rows where rating is higher then 5
p_df = r_df[(r_df['Rating'] <= 5) | (r_df['Rating'].isnull())]

#%% Reset index
p_df = p_df.reset_index(drop = True)

#%% Convert reviews column to numeric
p_df.Reviews = pd.to_numeric(p_df.Reviews)

#%% Gruping data by categories
g_df = p_df.groupby('Category').count()

#%% Plot numbers of app by categories
g_df['App'].sort_values(ascending = False).plot.bar(title= 'Categories')

#%% Gruping data by column type
g_df_type = p_df.groupby('Type').count()

#%% Plot numbers of app by types
g_df_type.App.plot(kind = 'pie', title = 'Apps by types', autopct='%1.1f%%')

#%% Group data by rating and calculate count and mean of rating
g_pivot = pd.pivot_table(p_df, index = ['Genres','Type'], \
                         aggfunc = {'Rating':['count', 'mean']})

#%% Create column by gruop indexes name
g_pivot['Joined_name'] = ['->'.join(g_pivot.index[numb]) for\
                          numb in range(g_pivot.index.size)]

#%% Set new index name
g_pivot = g_pivot.set_index(g_pivot['Joined_name'], drop=True)

#%% Remove Joined_name columns
del g_pivot['Joined_name']

#%% Rename pivot table columns name
g_pivot.columns = ['Rating_count','Rating_mean']

#%% Sort values in pivot tables by highest mean
g_pivot = g_pivot.sort_values('Rating_count', ascending = False)

#%% Remove form pivot table values where rating count is lower ther 100
g_pivot = g_pivot[g_pivot['Rating_count'] >= 100]

#%% Plot pivot table with subplots
g_pivot.plot(kind = 'bar', subplots = True)
plt.ylim(ymax = 4.6, ymin = 3.5)

#%% Crate data frame with top 5 counting apps
top_5_apps = r_df.groupby('App').count()['Reviews'].nlargest(n = 5)

#%% Plot 5 top most rated apps
top_5_apps.plot.barh(title = 'Top rated apps')