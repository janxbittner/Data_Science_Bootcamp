#%% Importing modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%% Load the data
r_data = sns.load_dataset('titanic')

#%% Transform survived column to yes and no values
r_data['surv_Y_N'] = r_data['survived'].apply(lambda x: 'Yes' if x == 1 else 'No')

#%% Plot bar char with passengers sex
r_data.groupby('sex').size().plot.bar(title = 'Passengers by sex')

#%% Plot on bar char survived and sex
r_data.groupby(['sex','surv_Y_N']).size().plot(kind= 'bar',\
                                               title = 'survived by sex')
    
#%% Plot propability of survive of each sex
r_data.groupby('sex').mean()['survived'].plot(kind = 'bar',\
                                              title = 'Propability of survive'
                                              ' by sex')

#%% Plot propability of survive of each passengers class
r_data.groupby('class').mean()['survived'].plot(kind = 'bar',\
                                              title = 'Propability'
                                                  ' of survive by'
                                                      ' passengers clas')
    
#%% Create pivot table
f_pivot = pd.pivot_table(r_data,values = 'survived',index = 'sex',\
                         columns= 'class',aggfunc= 'mean')
    
#%% Group age by age range
r_data['Age_by_range'] = pd.cut(r_data['age'], bins = 4, precision= 0)

#%% Create pivot table  
s_pivot = pd.pivot_table(r_data,values = 'survived', index\
                         = 'Age_by_range', columns = 'class', aggfunc = 'mean')

#%% Plot last pivot table
s_pivot.plot(kind = 'bar', title = 'Propability of survive by class and age')

#%% Create subplots with survived by sex
fig, ax = plt.subplots(1,2,sharey = True)
r_data.groupby(['sex','surv_Y_N']).size()['male'].plot(ax = ax[0], kind = 'bar')
r_data.groupby(['sex','surv_Y_N']).size()['female'].plot(ax = ax[1], kind = 'bar')
ax[0].legend(['men'])
ax[1].legend(['female'])

#%% Create pivot table with
age_pivot = pd.pivot_table(r_data,values = 'age', index = 'surv_Y_N',\
                           columns = 'sex', aggfunc= 'count')

#%% Create subplots with plot function
age_pivot.plot(subplots = True, kind = 'bar',sharey= True, layout = (1,2))

#%% Create pivot table with sevral aggregation functions
sev_pivot = pd.pivot_table(r_data, index = 'sex', columns='class',aggfunc= {'age':'mean','fare':'mean','survived': 'count'})
