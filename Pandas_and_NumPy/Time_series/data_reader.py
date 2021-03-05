#%% Importing modules
from pandas_datareader.data import DataReader
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%% Import data to dataframe
raw_uber = DataReader('UBER','stooq')

#%% Export imported data to csv
raw_uber.to_csv('./source_data/Uber.csv')

#%% Plot close Uber values 
raw_uber['Close'].plot()

#%% Create new sample with monthly periods and calculated mean
resampled_uber = raw_uber.resample('BM').mean()

#%% Plot resampled and raw close data on one plot
raw_uber['Close'].plot()
resampled_uber['Close'].plot(style = '--', color = 'green')

#%% Plot raw close values with shift on one plot
fig, ax = plt.subplots(3, sharex = True)
raw_uber['Close'].plot(ax = ax[0])
raw_uber['Close'].shift(100).plot(ax = ax[1])
raw_uber['Close'].shift(-100).plot(ax = ax[2])

ax[0].legend(['Input'])
ax[1].legend(['Shift by 100 days'])
ax[2].legend(['Shift by -100 days'])

#%% Calculate ROI index
ROI = 100 * (raw_uber.shift(15)/ raw_uber - 1)

#%% Plot ROI index
ROI['Close'].plot()

#%% Plot monthy mean, close values and dayly std on one graph

fig,ax = plt.subplots(2, sharex = True)
raw_uber['Close'].plot(ax = ax[0])
raw_uber['Close'].rolling(window = 30).mean().plot(ax = ax[0])
raw_uber['Close'].pct_change().rolling(16).std().plot(ax = ax[1])

ax[0].legend(['price','rolling mean'])
ax[1].legend(['rolling_std'])