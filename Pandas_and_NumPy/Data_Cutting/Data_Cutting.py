# Importing modules
import pandas as pd
import numpy as np

#%% DF.LOC FUNCTION

# Importing Data base
raw_db = pd.read_csv('./Data/houses.csv')

# From raw db choose only houses nearby sea and high value
near_sea = raw_db.query('(ocean_proximity == "NEAR BAY") & (median_house_value > 500000) ')

# Form raw db take rows with step 10 and every second columns
sample_data = raw_db[::10]

# Replace median income value if condition is false
