#%% Importing modules
import pandas as pd
import numpy as np
import pytz

#%% Create indexes started from 1st January 2020 with 200 days
normal = pd.date_range('01-01-2020',periods = 200)

#%% Create indexes started with first 100 buissnes day
buissnes = pd.date_range('01-01-2020',periods = 200, freq = 'B')

#%% Create indexes started from 1st January 2020 with first 100 8 hour shifts 
shifts = pd.date_range('01-01-2020 06:00:00',periods = 100, freq = '8H',tz = 'US/Arizona')
print('Last shifts starts on the:',shifts[-1])

#%% Calculate how thing we can produce in 2020 if one part take 1 day 2 hour and 43 minutes 
productions = pd.date_range('01-01-2020', end = '31-12-2020 23:59:59', freq = '1D2H43T',\
                            tz = 'Europe/Warsaw')
print(f'One can produce: {productions.size} parts.')
#%% Create list with all Europe time zones
all_tzs = list(pytz.all_timezones)
europe_tz = [tz for tz in all_tzs if tz.startswith('Europe')]

#%% Create indexes started from 1st January 2020 with 200 days
normal = pd.date_range('01-01-2020',periods = 200)

#%% Convert productions data indexes to Baku time zone
baku_production = productions.tz_convert(tz = 'Asia/Baku')

#%% Create a normal distributed 20 values
n_values = np.random.randn(20) 

#%% Create indexes started from 1st January 2020 with 1 minute interval
first_20 = pd.date_range('01-01-2020',periods = 20, freq = 'T', tz= 'Europe/Warsaw' )

#%% Create series with random normal 20 values and one minute time periods
connected_series = pd.Series(n_values, index = first_20 , name = 'randn values')

#%% Plot connected_series
connected_series.plot()

#%% Create series with periods
connected_series_with_periods = connected_series.to_period()

#%% Plot connected_series
connected_series_with_periods.plot()

#%% Create series with productions in baku
prod_baku = pd.Series(1,baku_production, name= 'quantity of parts')

#%% Create series with weekly productions in baku
week_prod_baku = prod_baku.resample('7D').sum()

#%% Plot weekly productions in baku
week_prod_baku.plot()