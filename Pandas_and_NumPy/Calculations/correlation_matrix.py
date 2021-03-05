#%% Importing modues
import pandas as pd
import seaborn as sns
sns.set()

#%% Import UBER stock data to data frame
uber_df = pd.read_csv('./source_data/UBER.csv', index_col= 0 )

#%% Remove Adj Close column
uber_df = uber_df.drop(['Adj Close','Volume'],axis=1)

#%% Create correlation matrix
correlation_matix = uber_df.corr()

#%% Print correlation values between open and close
print('Correlation between columns: Open and Close is:' , uber_df['Open'].\
      corr(uber_df['Close']))

#%% Create heatmap with correlation matrix
sns.heatmap(correlation_matix)
