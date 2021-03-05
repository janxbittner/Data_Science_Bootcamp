# -*- coding: utf-8 -*-

# Importing modules
import pandas as pd
import numpy as np

# Create random int list
Rand_list = np.random.randn(10,5)

# Create a random data frame
df = pd.DataFrame(Rand_list, columns=['1st','2nd','3rd','4th','5th'])

# Random function with replace some values with NaN
for row in df.values:
    number = np.random.choice([0,1,2,3,4])
    if number == 0 :
        number = np.random.choice([0,1,2,3,4])
        row[number] = np.nan
        
# Crating mask with contain bool values
mask = df.isnull()

# Create column with nan values
df['6th'] = np.nan

# Delete empty column
del df['6th']

# Delete na values
df = df.dropna()

# Random function with replace some values with NaN
for row in df.values:
    number = np.random.choice([0,1,2,3,4])
    if number == 0 :
        number = np.random.choice([0,1,2,3,4])
        row[number] = np.nan

# Fill na values
df = df.fillna('No data')
