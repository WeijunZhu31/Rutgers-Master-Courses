# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 12:27:40 2019

@author: Weijun
"""

#%% 
import numpy as np
import pandas as pd
# !pip install twitter
from twitter import Twitter
from twitter import OAuth

from pandas.io.json import json_normalize

#%%
apikey='LmWo260maj5KsmP3wnigGiymR'
apisecretkey='wdFhGB3XV79csLvSI57R1OFavsXNntbdtmlJzy2spNdMIFbnxn'
accesstoken='4012083173-pdPffs50tApeBURWR9QQt22rlhEp0sdEaCFwBvR'
accesstokensecret='PVwr62zsdUF0QQpcRMkPDBLxJ4HhAG4Cjccy49GwPv8pK'

#%%
oauth = OAuth(accesstoken, accesstokensecret, apikey, apisecretkey)
api = Twitter(auth = oauth)

#%%
help(api)

#%%
t_loc = api.trends.available()
print(t_loc)

#%%
df_loc = json_normalize(t_loc)

#%%
print(df_loc.country.value_counts())

#%%
dfNew = df_loc[df_loc['name'].str.contains('New')]
dfNew[['name','woeid']]

#%%
ny = dfNew.loc[dfNew.name == 'New York', 'woeid']

#%%
# get error!!!
ny_trend = api.trend.place(_id=ny)

#%%
type(ny)

#%%
ny.values

#%%
ny_trend = api.trends.place(_id=ny.values[0])
dfny = json_normalize(ny_trend)

#%%
dfny.trends

#%%
type(dfny.trends)

#%%
dfny.trends.shape

#%%
dftrends = json_normalize(dfny.trends.values[0])

#%%
dftrends.to_pickle('dftrends.pkl')

#%%
dftrends = pd.read_pickle('dftrends.pkl')

#%%
api.statuses.update(status='Their is an invasion at the border, some get Jon Snow')
mytweets = api.statuses.home_timeline()
dfmyt = json_normalize(mytweets)
mytweets1 = api.statuses.home_timeline(count = 1)
dfmyt1 = json_normalize(mytweets1)

#%%
dftrends.columns
dftrends.nlargest(5,'tweet_volume')[['name','tweet_volume']]

#%%
search_result = api.search.tweets(q='Trump',count=100,
                                  tweet_mode='extend')
dfsr = json_normalize(search_result)
#%%
dfst = json_normalize(dfsr.statuses.values[0])

#%%
df0 = pd.DataFrame({'Values':dfst.loc[0]})

#%%
# only loc works in conditional search！！
price = pd.Series([2,3,4,5,6])
fruit = pd.Series(['apple', 'orange', 'plum', 'cherry', 'mango'])
df = pd.DataFrame({'price' : price, 'fruit' : fruit})

df.loc[fruit == 'orange', 'price'] = 40

# iloc do not work in conditional search！！only loc！！
# df.iloc[df.fruit == 'orange']


#%%
a=pd.Series([5,4,3,2,1], index =['peach', 'orange', 'melon', 'cherry', 'apple'] )
b=pd.Series([50, 40, 30, 20, 10], index =['apple', 'cherry', 'melon', 'orange' , 'peach'])
df=pd.DataFrame({'a':a,'b':b})
x=sum(df.iloc[2,0:2])

#%%
# nan in dataframe
a=pd.Series([5,4,3,2,1], index =['peach', 'orange', 'melon', 'cherry', 'apple'] )
b=pd.Series([50, 40, 30, 10], index =['apple', 'cherry', 'melon', 'peach'])
df=pd.DataFrame({'a':a,'b':b})
x=sum(df.iloc[2,0:2])
y=df.iloc[2:4,0:2].sum()



