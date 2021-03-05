#%% Importing modules
import pandas as pd
import seaborn as sns
sns.set()

#%% Data import
URL = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00492'
'/Metro_Interstate_Traffic_Volume.csv.gz')

r_data = pd.read_csv(URL, index_col = "date_time", parse_dates = True)

#%% Select data form 1st January 2016
metro_df = r_data.loc['2016-01-01':]

#%% Create series with traffic
traffic = metro_df.iloc[:,-1:]

#%% Resample date form hour to monthly and calulate frequency
traffic_resampled = traffic.resample('M').sum()

#%% Rename series name
traffic_resampled.columns = ['Monthly traffic volume']

#%% Plot traffic values
traffic_resampled.plot()

#%% Create pivot table 
metro_pivot = pd.pivot_table(metro_df, values = 'traffic_volume', index = \
                             'weather_main',)
    
#%% Plot traffic values depend of weather
metro_pivot.plot(kind = 'bar')
