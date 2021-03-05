#%% Importing modules
import pandas as pd
import numpy as np

#%% Create series with stocks
stocks = pd.Series(['Apple', np.nan, 'gOOgle','INtEl','microsoft    ', '   amaZon']\
                   ,name = 'Stocks')

#%% Whitespace removal
stocks = stocks.str.strip()

#%% Capitalize names
stocks = stocks.str.capitalize()

#%% Create data frame with random values
rand_df = pd.DataFrame(np.random.rand(10,2),columns = ["   ColUMN A  "\
                       ,"        COLUMN b     "])

#%% Normalize columns name
rand_df.columns = rand_df.columns.str.strip()
rand_df.columns = rand_df.columns.str.upper()
rand_df.columns = rand_df.columns.str.replace(' ','_')

#%% 
"""HASHTAGS ANALISYS"""

#%% Create series with hashtags
hash_series = pd.Series(['#tagblender#hungry#foodgasm#instafood#instafood#yum',\
                         '#singer#hardrock#tagblender#guitarist#pianist',\
                             '#dogoftheday#pet#pets#dogsofinstagram#ilovemydog'],\
                        name = 'Hashtags',index = ['Food','Music','Dog'])

#%% Split the hashtags
hash_series = hash_series.str.split('#')

#%% Remove empty objects form list
hash_series = hash_series.apply(lambda x: [element for element in x if len(element) > 0])

#%% Create df with hashtags
hash_df = pd.DataFrame(pd.DataFrame(hash_series)["Hashtags"].to_list(),\
                       index= hash_series.index)

#%% Create df by get function
hash_series_val = pd.Series()
for num in hash_df.columns:
    hash_series_val = hash_series_val.append(hash_df[num],ignore_index = True)

#%% Remove nan values from series
hash_series_val = hash_series_val.dropna()

#%% Conect all values in series using space separator
conected = " ".join(hash_series_val)

#%% Create series form string
words_series = pd.Series('#love#instagood#me#cute#tbt#photooftheday#instamood#iphonesia'\
                         .split('#'),name = 'Words')
    
#%% Remove first index
del words_series[0]

#%% Reset index
words_series = words_series.reset_index()

#%% Remove first column
words_series = words_series.drop('index', axis = 1)

#%%  
'''REGULAR EXPRESSION WITH SERIES'''

#%% String with websites name
string = 'Bitly,Rebrandly,Polr,TinyURL,BL.INK,Hyperlink,T2M,URL,Yourls,Shorby'

#%% Creates series with websites name
web_series = pd.Series(string.split(','),name = 'Webpages')

#%% Create series when true is where name contain any number
number_logic_series = web_series.str.contains(r'[0-9]')

#%% Create series that contain names of websites with any number
sites_with_nb = web_series[web_series.str.contains(r'[0-9]')]

#%% Create series that contain b letter in websites
sites_with_b = web_series[web_series.str.contains(r'[b]')]

#%% Create series that contain URL letter in websites
sites_with_url = web_series[web_series.str.contains('URL')]
