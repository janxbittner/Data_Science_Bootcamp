# -*- coding: utf-8 -*-
# Importing modules
import pandas as pd
import numpy as np

#%% Basics of Series

# Example 1  Scalar

scalar = pd.Series(4)

# Example 2 Salary

Salary_avg = pd.Series([50000,75000,100000],["Junior DS",'Regular DS','Senior DS'],name = "Annual wages")

# Example 3 Car and Models with dict

Car_models_list =pd.Series({'Volvo':'V40',"Renault":"Captur","Mercedes":"GLB"},\
                           name= "Model")
    
# Example 4 Random 10 Numbers

rand_series = pd.Series([np.random.randint(1,7) for value in range(1,11)],index = range(1,11)
                        ,name= 'Random Value')

# Example 5 Taking only values form series data

rand_values = rand_series.values

# Example 6 Check if we roll 6 in rand_series

#print('Yes we roll 6!') if 2 in rand_series.values else print("Maybe next time...")

# Example 7 return first 3 rolls

first_three = rand_series[:3]

# %% Operations on series:

#Example 8 check data type in Series

#print(Salary_avg.dtype)

#Example 9 print the third element in Series using iloc:

#print(Salary_avg.iloc[2])
#print(Salary_avg[2])

DS_index = Salary_avg.index
DS_name = Salary_avg.name
DS_size = Salary_avg.shape

# %% Example 10 create 2 Data series with roll dice and calculate and print it's sum

First_roll = pd.Series(np.random.randint(1,7,6),index = range(1,7), name= 'Result')
Second_roll = pd.Series(np.random.randint(1,7,6),index = range(1,7), name= 'Result')

Sum_of_roll = First_roll.add(Second_roll)
print(Sum_of_roll)

# %% Example 11 Remove nan values and duplicates from Series

Random_series = pd.Series(np.random.randint(1,10,100),index = range(1,101), name= 'Values')

# Random changing values in Series to nan

for index,element in Random_series.items(): Random_series[index] = np.nan\
    if element == np.random.randint(1,10) else element

# Remove nan values from series
Random_series = Random_series.dropna()

# Remove dupcitates from series
Random_series = Random_series.drop_duplicates()

# Sort series 
Random_series = Random_series.sort_values()


#%% Exercise 12 Create histogram of sample data

Histogram_data = pd.Series(np.random.randn(10000))
Histogram_data.hist(bins=100)

#%% Exercise 13 Read text data, create series and print some statistics data

unit_cost_text = ''' 1.99 
 19.99 
 4.99 
 19.99 
 2.99 
 4.99 
 1.99 
 4.99 
 1.99 
 8.99 
 4.99 
 1.99 
 19.99 
 4.99 
 125.00 
 15.99 
 8.99 
 8.99 
 19.99 
 4.99 
 1.29 
 15.99 
 8.99 
 15.00 
 4.99 
 19.99 
 4.99 
 1.99 
 4.99 
 1.29 
 8.99 
 125.00 
 4.99 
 12.49 
 23.95 
 275.00 
 1.29 
 1.99 
 19.99 
 1.29 
 4.99 
 19.99 
 4.99''' 

# Create list with unit_cost value
unit_list = [float(value.strip()) for value in unit_cost_text.split('\n')]

# Create data Series
unit_series = pd.Series(unit_list,name = "Unit Cost" )

# Print basic Statistics information
print("Basic Statistics Information:\n")
print(unit_series.describe())

# Print histogram
unit_series.hist(bins = 100,color = 'red')

#Print conclusion
print('\nMost of Units cost are around 25 value. Because of 3 elemenents:')
print(unit_series.nlargest(3))
print("\nMean is much higher then median!. This function is Right-Skewed!")

#%% AGREGATION

#%% Exercise 14 using unit_series form Exercise 13 print Series data with mean,
#  median, min,max

print(unit_series.aggregate([np.mean,np.median,'min','max']))

#%%  Exercise 15: return numbers of element with provide required std value in random
# int data series

std_reqiured = input('Enter required std value:')
times_of_loop = 1
current_std = 0
try:
    std_reqiured = float(std_reqiured)
    
    while current_std < std_reqiured and current_std != np.nan:
    
        random_data = pd.Series(np.random.randn(times_of_loop+1))
        current_std = random_data.aggregate(np.std)
        if times_of_loop < 1000:
            times_of_loop += 1
        else:
            print('Can\'t reach value, because in high volume of dat std'\
                  +' value is close to 1.')
            break
        
    

    print('To  get required std values, program generate',times_of_loop,\
      'random elements.')

except:
    print('Wrong value, can\'t convert to float')
    

print(random_data.aggregate([np.std,'min','max']))
    
#%% Apply method do function to every elements of series
np.random.seed(0) # provide everytime the same random values
base_dt = pd.Series(np.random.randn(20))
bin_simple = base_dt.apply(lambda x: 1 if x > 0 else 0)
std_dt = base_dt.apply(lambda x: (x - np.mean(base_dt)) / np.std(base_dt))
sigmoid = std_dt.apply(lambda x : 1 / (1/1 + np.exp(x)))

#%% Importing data


#%% Exercise 16: load tesla stocks from csv file to data frame and create series
#  with only high column. Set data to index column. 
#Export high series to csv file with header

data_frame = pd.read_csv('./Data/TSLA.csv', index_col = 0)
High_series = pd.Series(data_frame["High"])

High_series.to_csv('.\Data\high_value.csv',header= ['High values!'])


#%% Exercise 17: Import data form clipboard do sth and export sth to sth
Df_from_clipboard = pd.read_clipboard()
Df_from_clipboard.to_csv('.\Data\stocks.csv')

#%% Case Study:
'''
1. Import data from csv file to Data frame.
2.Set data column as index column.
3. Create data series from Close column, but use only data from 1st January 2010.
4. Create figures form created data series, and second one with logarythim scale
and figure name.
5. Save figure to png file using matplotlib.
6. Export data series to csv.


'''


Amz_stocks_df = pd.read_csv('./Data/amzn_us_d.csv',index_col = 0)

Close_val = pd.Series(Amz_stocks_df['Close'])

Close_val = Close_val['2010-01-01':]

Close_val.plot()

Close_val.plot(logy = True,title = "Close values figure.")

import matplotlib.pyplot as plt
plt.savefig('./Close_fig.png',format = 'png')

Close_val.to_csv('./Data/amzn_close.csv',header = ['Amazon Close Values'])

#%%  Case study 2
'''
1. Create Series form FTSE_100_company_names.
2. Standarize names.
3. Chcek if Halma is in FTSE_100.
4. Create list with companies name lenght less the 5 characters.
'''
FTSE_100_company_names = ['3i', 'Land Securities', 'Halma', 'DS Smith', 'Antofagasta',
                      "St. James's Place plc", 'Kingfisher plc', 'SSE plc',
                      'Anglo American plc', 'Sage Group', 'Intertek', 'Segro',
                      'Aveva', 'Whitbread', 'Bunzl', 'Prudential plc', 'Glencore',
                      'Smurfit Kappa', 'DCC plc', 'M&G', 'Hikma Pharmaceuticals',
                      'Royal Bank of Scotland Group', 'Compass Group', 'Ocado',
                      'Just Eat', 'Rio Tinto Group', 'International Airlines Group',
                      'Unilever', 'JD Sports', 'WPP plc', 'Carnival Corporation &plc',
                      'Rightmove', 'Ashtead Group', 'Standard Chartered', 'BP',
                      "Sainsbury's", 'Croda International', 'Severn Trent',
                      'Experian', 'Next plc', 'British American Tobacco',
                      'Rentokil Initial', 'Coca-Cola HBC', 'Melrose Industries',
                      'Burberry', 'Meggitt', 'Berkeley Group Holdings',
                      'Scottish Mortgage Investment Trust', 'BT Group',
                      'Reckitt Benckiser', 'GlaxoSmithKline', 'National Grid plc',
                      'Imperial Brands', 'Rolls-Royce Holdings', 'BAE Systems',
                      'Vodafone Group', 'HSBC', 'London Stock Exchange Group', 
                      'ITV plc', 'Phoenix Group', 'Barclays', 'TUI Group',
                      'Auto Trader Group', 'United Utilities', 'CRH plc',
                      'NMC Health', 'Aviva', 'Mondi', 'Associated British Foods',
                      'RSA Insurance Group', 'Informa', 'RELX',
                      'Barratt Developments', 'Persimmon plc', 'Diageo',
                      'Morrisons', 'Ferguson plc', 'Lloyds Banking Group',
                      'EasyJet', 'Legal & General', 'BHP', 'Royal Dutch Shell',
                      'Evraz', 'Polymetal International', 'Johnson Matthey',
                      'Smith & Nephew', 'InterContinental Hotels Group',
                      'Spirax-Sarco Engineering', 'British Land', 'Taylor Wimpey',
                      'Flutter Entertainment', 'Pearson plc', 'Hargreaves Lansdown',
                      'Smiths Group', 'Admiral Group', 'Schroders', 'AstraZeneca',
                      'Standard Life Aberdeen', 'Centrica', 'Tesco']

FTSE_100_names = pd.Series(FTSE_100_company_names,name = 'FTSE 100 company names')
FTSE_100_names_nomrlized = FTSE_100_names.apply(lambda name : name.upper().replace(' ','_'))

print('Halma is in FTSE 100' if 'HALMA' in FTSE_100_names_nomrlized.values else\
      'Halma isn\'t in FTSE 100')

short_names = [name for name in FTSE_100_names_nomrlized if len(name) < 5]