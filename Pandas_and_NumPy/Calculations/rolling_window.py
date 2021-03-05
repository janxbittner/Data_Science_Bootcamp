#%% Importing modues
import pandas as pd
import seaborn as sns
import numpy as np
sns.set()

#%% Import Alphabet stock data to data frame
alpha_df = pd.read_csv('./source_data/GOOG.csv', index_col= 0, nrows = 1000 )

#%% Create price df with some alphabet values
price_df = alpha_df[['Open','High','Low','Close']]

#%% Create dataframe with Alphabet stock volume
volume = alpha_df['Volume']

#%% Calculate cumulated sum of volume
cum_vol = volume.cumsum()

#%% Plot cumulate sum of volume
cum_vol.plot()

#%% Create series with alphabet close values
close = alpha_df['Close']

#%% Calculate moving average time periods = 90 days
close_roll_avg = close.rolling(window = 90).mean()

#%% Plot moving average with close values
close_roll_avg.plot(style = 'r--', title = 'Moving avergage')
close.plot()

#%% Plot moving averages of given time periods
close.plot(style = 'k')
time_periods = [5,10,30,60,90]
for time in time_periods:
    close_roll_avg = close.rolling(window = time).mean()
    close_roll_avg.plot(alpha = 0.5)

#%% Plot moving minimum and maximum values of close
close.plot(style = 'k')
time_periods = [5]
for time in time_periods:
    close_roll_min = close.rolling(window = time).min()
    close_roll_min.plot(alpha = 0.5)
    close_roll_max = close.rolling(window = time).max()
    close_roll_max.plot(alpha = 0.5)
    
#%% Plot moving averages of values in price_df
price_roll_avg = price_df.rolling(window = 5).mean().plot(alpha = 0.5)
close.plot(color = 'black')

#%% Plot standard deviation and close values of stock
close_rolling_std = close.rolling(window =5).std().plot()
close.plot()

#%% Create subplots with values from price_df
price_df.plot(subplots = True)

#%% Plot sigmoid of close values
Avg_roll_avg = close.rolling(window = 1).apply(lambda v : (v - price_df['Close'].aggregate('mean'))/price_df['Close'].aggregate(np.std)).plot()
