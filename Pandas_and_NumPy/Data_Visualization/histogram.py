#%% Importing modues
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()

#%% Create data frame with random 1000 elements
rand_df = pd.DataFrame(np.random.rand(1000))

#%% Create histogram
rand_df.hist(bins = 10)

#%% Create data frame with 3 columns with random 1000 elements
rand_3_df = pd.DataFrame({'mu-0_sigma-1': np.random.randn(1000),
                          'mu-1_sigma-2': 2 * np.random.randn(1000) + 1,
                          'mu-8_sigma-3': 3 *np.random.randn(1000) + 8,})
    
#%% Plot the multiple histogram
rand_3_df.plot(kind = 'hist', bins = 100, cmap = 'cividis', title =\
               'Different normal distributions')

#%% Plot the multiple histogram with cumulative
rand_3_df.plot.hist(cumulative = True, bins = 100, cmap = 'cividis')

#%% Plot 3 histogram on one graph
rand_3_df.hist(sharex = True,sharey = True, bins = 100, color = 'red')